import utils
import time
import asyncio
import aiohttp

"""
由于requests不支持异步爬虫,因此需要使用aiohttp,但这个语法有点难懂...
"""
async def async_spider(url):
    async with aiohttp.ClientSession() as session: # 创建一个异步爬取的对象
        async with session.get(url) as resp:
            result = await resp.text()
            print(f"crwa url:{url},{len(result)}")
    
loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(async_spider(url))
    for url in utils.urls
    ]
start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print(f"耗时{end-start}s")