import asyncio

async def func():
    print("我是协程函数")

"""
①创建事件循环
②把任务放进去
"""
# py3.5~3.6
loop = asyncio.get_event_loop()
loop.run_until_complete(func()) 

# py3.7以后的写法
# asyncio.run(func())