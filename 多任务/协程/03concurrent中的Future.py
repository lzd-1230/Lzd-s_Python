from concurrent.futures import Future
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

"""
这个对象是给进程池和线程池等待结果用的:
    因为很多第三方模块软件目前还不支持这种异步
    因此需要把线程池和进程池返回的Future对象,转换成asyncio类型的对象
    解决方案:使用 loop.run_in_executor()函数来创建事件循环,实际上就是多线程的原理...没必要硬用asyncio
"""




