import requests
import datetime

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


get_service_id_max_request()
