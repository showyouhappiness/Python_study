def test():
    print('--------test-------------')


def func(f):
    print(f)
    f()
    print('-----------func------------')


func(test)
