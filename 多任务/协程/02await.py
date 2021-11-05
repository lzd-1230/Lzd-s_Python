
import time
import asyncio

async def others(i):
    print(f"{i}start")
    await asyncio.sleep(2) # IO中
    print(f"{i}end")
    return "IO返回"

async def main():
    task_list = [
        asyncio.create_task(others(i),) # 获取协程对象的时候可以直接传递参数
        for i in range(5)
    ]
    # 主线程的阻塞
    print("主线程阻塞")
    time.sleep(1)
    print("主线程阻塞完毕")
    done, pending = await asyncio.wait(task_list,timeout=5) # pending表示规定时间内未完成的任务
    print(done)

asyncio.run(main())