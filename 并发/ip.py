import time

import requests
from pyecharts.components import Table
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED, ALL_COMPLETED

headers = {
    'token': '9fee1659eaf8f9065bf723c3b02452db',
    'projectname': 'msgcloud-platform',
    'appname': 'main_srv2',
}

json_data1 = {
    'app_mark': '1320_5207_main_srv2',
    'env': 'prod',
    'query_tag_type': 'dst_logic_id',
    'begin_time': '2022-05-26 00:00:00',
    'end_time': '2022-05-26 12:00:00',
    'metric': 'dst_req_cnt',
    'tag_set': {
        'original_appid': {
            'val': [
                '1120019',
            ],
        },
    },
}
yewu_id='1120019'
response = requests.post('http://openapi.zhiyan.oa.com/monitor/v2/api/chart/sub_dimens/query', headers=headers,
                         json=json_data1)
app_id_list = response.json()['data']['tag_info']['tag_list']
dict = {"dst_logic_id": yewu_id, "original_appid": app_id_list}


def get_result(value):
    json_data2 = {
        "app_mark": "1320_5207_main_srv2",
        "sec_lvl_name": "default",
        "env": "prod",
        "is_english": "yes",
        "is_together": True,
        "tag_set": [
            {
                "key": "dst_logic_id",
                "value": [
                    value
                ]
            },
            {
                "key": "original_appid",
                "value": [
                    dict['dst_logic_id']
                ]
            }
        ],
        "metric_name": "dst_req_cnt",
        "begin_time": "2022-05-26 00:00:00",
        "end_time": "2022-05-26 23:59:59",
        "gap": 1,
        "page_num": 1,
        "limit": 9,
    }

    response = requests.post('http://openapi.zhiyan.oa.com/monitor/v2/api/chart/info/query', headers=headers,
                             json=json_data2)
    resp_body = response.json()
    current_list = []
    data_list = resp_body['data']['chart_info'][0]['detail_data_list']
    for data in data_list:
        if data['current']:
            current_list.append(data['current'])
    if current_list:
        current_list_ten[value] = sorted(current_list, reverse=True)[0]


current_list_ten = {}
now=time.time()
with ThreadPoolExecutor(max_workers=100) as t:
    all_task = [t.submit(get_result, value) for value in dict['original_appid']]
    wait(all_task, return_when=ALL_COMPLETED)
print(time.time()-now)

x = sorted(current_list_ten.items(), key=lambda x: x[1], reverse=True)
headers = ['appid', 'maxrequest']
table = Table()
table.add(headers, x)
table.render("xinan_workload2.html")
