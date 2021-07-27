from _ctypes import PyObj_FromPtr


def di(obj_id):
    """ 通过变量ID 得到变量的值"""
    return PyObj_FromPtr(obj_id)


if __name__ == "__main__":
    i = {"j": 99, "name": "jack"}
    var_id = id(i)
    print(var_id)
    print(di(var_id))
