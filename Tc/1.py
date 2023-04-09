import requests
import pymysql
import datetime
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED


def call_interface(params):
    response = requests.post('http://openapi.zhiyan.oa.com/monitor/v2/api/chart/info/query', headers=request_headers,
                             json=params)
    try:
        data_list = response.json()['data']['chart_info'][0]['detail_data_list']
        print(data_list)
        request_list = []
        for data in data_list:
            if data['current']:
                request_list.append(data['current'])

        if request_list:
            required_data = sorted(request_list, reverse=True)[0]
            return required_data
    except Exception as e:
        print("get data have error:", e)
        return None


# 通过Appid获取调用的service_id
def get_service_id(app_id=None):
    Get_service_id_params = {
        'app_mark': '1320_5207_main_srv2',
        'env': 'prod',
        'query_tag_type': 'dst_logic_id',
        'begin_time': begin_time,
        'end_time': end_time,
        'metric': 'dst_req_cnt',
        'tag_set': {
            'original_appid': {
                'val': [
                    app_id
                ],
            },
        },
    }

    response = requests.post('http://openapi.zhiyan.oa.com/monitor/v2/api/chart/sub_dimens/query',
                             headers=request_headers,
                             json=Get_service_id_params)
    try:
        service_id_list = response.json()['data']['tag_info']['tag_list']
        return service_id_list
    except Exception as e:
        print(app_id, "have error:", e)
        return None


# 获取单个app_id 中 每个service_id 的最大请求量
def get_service_id_max_request(service_id=None, app_id=None):
    service_id_max_params = dict(common_param, **{
        "tag_set": [
            {
                "key": "dst_logic_id",
                "value": [
                    service_id
                ]
            },
            {
                "key": "original_appid",
                "value": [
                    app_id
                ]
            }
        ],
    })
    service_max = call_interface(service_id_max_params)
    return service_max


# 获取Appid当天最大请求量
def get_appid_max_request(app_id=None):
    Appid_max_params = dict(common_param, **{
        "app_mark": "1320_5207_main_srv2",
        "metric_name": "req_cnt",
        "tag_set": [
            {
                "key": "logic_id",
                "value": [
                    app_id
                ]
            }
        ]
    })
    app_max = call_interface(Appid_max_params)
    return app_max


# 获取service_id的总请求量
def get_service_all_request(service_id=None):
    service_all_params = dict(common_param, **{
        "tag_set": [
            {
                "key": "dst_logic_id",
                "value": [
                    service_id
                ]
            }
        ]
    })
    service_all = call_interface(service_all_params)
    return service_all


def get_name_from_DB(value=None):
    conn = pymysql.connect(host='9.146.191.237',
                           user='msgcloud_readonly',
                           password='msgcloud',
                           db='msgcloud',
                           charset='utf8'
                           )
    cur = conn.cursor()
    sqli = 'select cn_name,admin_group from msgcloud_t_components where component_id = %s ' % value
    cur.execute(sqli)
    a = cur.fetchone()[0]
    return a


def get_appid_from_DB():
    conn = pymysql.connect(host='9.146.191.237',
                           user='msgcloud_readonly',
                           password='msgcloud',
                           db='msgcloud',
                           charset='utf8'
                           )
    cur = conn.cursor()
    sqli = 'select app_id from msgcloud_t_business'
    result = cur.execute(sqli)
    a = cur.fetchall()
    b = [str(i[0]) for i in a if i[0]]
    return b


def updata_data_to_DB(value_list=None):
    conn = pymysql.connect(host='11.181.61.221',
                           user='infosec',
                           password='resource',
                           db='resource_assess',
                           charset='utf8'
                           )
    cur = conn.cursor()
    conn.select_db('resource_assess')
    spli = 'insert into resource (appid,service_id,service_name,appid_service_max,appid_max,service_id_all,appid_service_percent,service_all_percent,valid,data_time)' \
           ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    try:
        cur.execute(spli, value_list)
        conn.commit()
    except Exception as e:
        conn.rollback()
        cur.close()


# 使用线程调用每一组对应的所有值
def get_request(app_id, data_valid=1):
    # 获取app_id最大值
    app_max = get_appid_max_request(app_id)
    if app_max is None or app_max < 100000:
        return
    print(app_id, app_max)
    # 根据app_id获取与之对应的service_id_list
    Service_id_list = get_service_id(app_id)
    for service_id in Service_id_list:
        if service_id == '0':
            continue
        # 获取service_id最大值
        appid_service_max = get_service_id_max_request(service_id, app_id)
        print(appid_service_max)
        # 获取service_id的所有值
        service_all = get_service_all_request(service_id)
        # 获取中文名
        chinese = get_name_from_DB(service_id)
        # 获取service_id最大请求量占Appid最大请求量的调用百分比
        service_appid_percent = "%.2f" % (appid_service_max / app_max * 100)
        # 获取appid中一个service_id最大请求量占所有service的调用百分比
        service_all_percent = "%.2f" % (appid_service_max / service_all * 100)
        one_app_list = [app_id, service_id, chinese, appid_service_max, app_max, service_all, service_appid_percent,
                        service_all_percent, data_valid, yes_time]
        # updata_data_to_DB(one_app_list)


if __name__ == '__main__':
    yes_time = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')
    begin_time = yes_time + " 00:00:00"
    end_time = yes_time + " 23:59:59"
    request_headers = {
        'token': '9fee1659eaf8f9065bf723c3b02452db',
        'projectname': 'msgcloud-platform',
        'appname': 'main_srv2',
    }

    common_param = {
        "app_mark": "1320_5207_main_srv2",
        "sec_lvl_name": "default",
        "env": "prod",
        "is_english": "yes",
        "is_together": True,
        "metric_name": "dst_req_cnt",
        "begin_time": begin_time,
        "end_time": end_time,
        "gap": 1,
        "page_num": 1,
        "limit": 1
    }
    Appid_list = get_appid_from_DB()
    for Appid in Appid_list:
        with ThreadPoolExecutor(max_workers=100) as t:
            all_task = [t.submit(get_request, Appid)]
            # wait(all_task, return_when=ALL_COMPLETED)
