class PathLoggerMiddleware:
    # 这里的__init__方法是必须要有的，用于接收get_response参数
    def __init__(self, get_response):  # get_response是从django传入的一个参数，用于获取响应
        self.get_response = get_response

    # 这里的__call__方法是必须要有的，用于处理请求
    def __call__(self, request):
        # 这里的request是django.http.request.HttpRequest类的实例
        # 在处理请求之前的代码
        print("Before function execution")
        print(f"Request path: {request.path}")
        response = self.get_response(request)
        print(response)
        # 在处理请求之后的代码
        print("After function execution")
        return response
