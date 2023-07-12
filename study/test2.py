# # coding:utf-8
# import time
# import redis
#
# rc = redis.StrictRedis(host='localhost', port='6379', db=3, password='1q2w3e4r5t')
# ps = rc.pubsub()
# ps.subscribe('liao')  # 从liao订阅消息
# for item in ps.listen():  # 监听状态：有消息发布了就拿过来
#     if item['type'] == 'message':
#         print(item['channel'])
#         print(item['data'])

# coding:utf-8
# 定义字典
article_all = {}
article_info = {}

import random
import json

for i in range(1, 6):
    data1 = json.loads(json.dumps(article_all))
    all_sum = 0
    one_sum = 0
    for j in range(1, 11):
        all = random.randint(900, 1200)
        one = random.randint(900, all)
        all_sum = all_sum + all
        one_sum = one_sum + one
        data = json.loads(json.dumps(article_info))
        data[str(j)] = {
            'all': all,
            'one': one,
            'rate': round(one / all, 4) * 100,
            'diff': all - one,
        }
        data1.update(data)
    data1['all_sum'] = all_sum
    data1['one_sum'] = one_sum
    data1['diff_sum'] = all_sum - one_sum
    data1['rate_sum'] = round(one_sum / all_sum, 4) * 100

    maybe = random.uniform(0.7, 0.8)
    data1['maybe'] = int(maybe*all_sum)
    data1['maybe_rate'] = round(maybe, 4) * 100
    data1['maybe_diff'] = int(one_sum - maybe*all_sum)
    data1['maybe_diff_rate'] = round((one_sum - maybe*all_sum)/all_sum, 4) * 100
    data1['defect'] = {
        'ss': {
            'rate': '{:.2f}'.format(random.uniform(0.4, 0.5)),
            'Number': int(random.uniform(0.4, 0.5)*(all-one)),
        },
        'qk': {
            'rate': '{:.2f}'.format(random.uniform(0.2, 0.3)),
            'Number': int(random.uniform(0.2, 0.3)*(all-one)),
        },
        'sk': {
            'rate': '{:.2f}'.format(random.uniform(0.08, 0.1)),
            'Number': int(random.uniform(0.08, 0.1)*(all-one)),
        },
        'jbz': {
            'rate': '{:.2f}'.format(random.uniform(0.07, 0.09)),
            'Number': int(random.uniform(0.07, 0.09)*(all-one)),
        },
        'gmjz': {
            'rate': '{:.2f}'.format(random.uniform(0.04, 0.06)),
            'Number': int(random.uniform(0.04, 0.06)*(all-one)),
        },
        'lw': {
            'rate': '{:.2f}'.format(random.uniform(0.04, 0.05)),
            'Number': int(random.uniform(0.04, 0.05)*(all-one)),
        },
        'dz': {
            'rate': '{:.2f}'.format(random.uniform(0.02, 0.03)),
            'Number': int(random.uniform(0.02, 0.03)*(all-one)),
        },
        'zl': {
            'rate': '{:.2f}'.format(random.uniform(0.01, 0.02)),
            'Number': int(random.uniform(0.01, 0.02)*(all-one)),
        },
        'mk': {
            'rate': '{:.2f}'.format(random.uniform(0, 0.01)),
            'Number': int(random.uniform(0, 0.01)*(all-one)),
        },
    }

    # 行缩进和键值排序
    json_dict_2 = json.dumps(data1, indent=2, sort_keys=False, ensure_ascii=False)
    print(json_dict_2)
