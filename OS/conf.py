import json
import os

path = os.getcwd()

conf_path = os.path.join(path, 'resources/config.json')

with open(conf_path, 'r', encoding='utf8')as fp:
    json_data = json.load(fp)


for key, value in json_data.items():
    exec("{} = value".format(key))