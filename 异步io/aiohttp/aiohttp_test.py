import asyncio
from aiohttp import web


async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body='<h1>Index</h1>'.encode(), content_type='text/html')


async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), content_type='text/html')


async def init(loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)
    app_runner = web.AppRunner(app)
    await app_runner.setup()
    # srv = await loop.create_server(app(), '127.0.0.1', 8080)
    srv = await loop.create_server(app_runner.server, '127.0.0.1', 8080)
    print('server started at http://127.0.0.1:8080...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
