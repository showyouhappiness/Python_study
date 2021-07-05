import threading
import asyncio


@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())


def runEventLoop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tasks = [hello(), hello()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


loop = asyncio.get_event_loop()
runEventLoop()
asyncio.set_event_loop(loop)
