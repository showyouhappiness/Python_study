import json

key_list = []


def generate_file():
    with open('C:\\Users\\Administrator\\.crf-config.json', 'r') as f:
        read_result = json.loads(f.read())
        return read_result


result = {
    "key1": "value1",
    "key2": {
        "nested_key1": "nested_value1",
        "nested_key2": "nested_value2"
    },
    "key3": [
        {"nested_key3-1": "nested_value3-1", "nested_key3-2": "nested_value3-2", "nested_key3-3": "nested_value3-3"},
        {"nested_key4": "nested_value4"}
    ]
}


def get_dict_all_keys(data):
    keys = set()
    if isinstance(data, dict):
        keys.update(data.keys())
        for value in data.values():
            keys.update(get_dict_all_keys(value))
    elif isinstance(data, list):
        for item in data:
            keys.update(get_dict_all_keys(item))
    return keys


def get_all_values(data):
    values = set()
    if isinstance(data, dict):
        for value in data.values():
            if isinstance(value, (dict, list)):
                values.update(get_all_values(value))
            else:
                values.add(value)
    elif isinstance(data, list):
        for item in data:
            values.update(get_all_values(item))
    return values


print(get_all_values(generate_file()))
