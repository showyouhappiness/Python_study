import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, "http://httpbin.org/headers")
        print(html)


asyncio.run(main())

"""输出结果：
{
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "Python/3.7 aiohttp/3.6.2"
  }
}
"""
