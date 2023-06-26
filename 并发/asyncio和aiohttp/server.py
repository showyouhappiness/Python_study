from aiohttp import web


async def handle(request):
    name = request.match_info.get('name', "Anonymous")  # 从请求中获取参数
    text = "Hello, " + name
    return web.Response(text=text)


app = web.Application()  # 创建一个应用
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])  # 添加路由

if __name__ == '__main__':
    web.run_app(app)  # 运行应用
