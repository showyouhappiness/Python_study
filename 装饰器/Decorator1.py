# 装饰器示例
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@logger
def add(a, b):
    return a + b


result = add(2, 3)
print(result)


# 类装饰器示例
class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Calling function: {self.func.__name__}")
        return self.func(*args, **kwargs)


@Logger
def multiply(a, b):
    return a * b


result = multiply(2, 3)
print(result)
