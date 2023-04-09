import requests

modelid_list = ['8130129', '8130141', '8130120', '8130005', '8130021', 8130242, 8130146, 8130020, 8130019, 8130153, 8130121,
                8130085, 8130095, 8130059, 8130096, 8130094, 8130164, 8130020, 8130035, 8130084, 8130178, 8130090,
                8130098, 8130125, 8130005, 8130071, 8130126, 8130156, 8130173, 8130189, 8130190, 8130191, 8130197, ]
for modelid in modelid_list:
    headers = {
        'token': '9fee1659eaf8f9065bf723c3b02452db',
        'projectname': 'msgcloud-platform',
        'appname': 'main_srv2',
    }

    json_data = {
        "app_mark": "1320_5207_main_srv2",
        "sec_lvl_name": "default",
        "env": "prod",
        "is_english": "yes",
        "is_together": True,
        "tag_set": [
            {
                "key": "service_name",
                "value": [
                    "MainSrv_Model"
                ]
            },
            {
                "key": "logic_id",
                "value": [
                    modelid
                ]
            },
            {
                "key": "original_appid",
                "value": [
                    "3720014"
                ]
            }
        ],
        "metric_name": "req_cnt",
        "begin_time": "2022-06-24 00:00:00",
        "end_time": "2022-06-24 23:59:59",
        "gap": 1,
        "page_num": 1,
        "limit": 1
    }

    response = requests.post('http://openapi.zhiyan.oa.com/monitor/v2/api/chart/info/query', headers=headers,
                             json=json_data)
    data_list = response.json()
    print(data_list)
