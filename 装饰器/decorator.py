def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function execution")
        result = func(*args, **kwargs)
        print("After function execution")
        return result

    return wrapper


@my_decorator
def my_function():
    print("Inside my_function")


my_function()
