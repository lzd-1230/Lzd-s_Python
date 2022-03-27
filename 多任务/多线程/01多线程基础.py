"""
python多线程的特点:
    python解释器自带了GIL全局锁,也即在任意时刻仅允许执行一个线程
    因此在计算密集型的任务中,我们还是希望使用多个CPU核心,而不是多线程(?????)
    在编程的时候要注意给每一个线程执行的机会(灵活使用sleep方法)
本代码讨论如何构造一个实用性最普遍的线程类,其独立于python中任何一种并发机制
"""
import time
from threading import Thread

class mytask():
    def __init__(self):
        self._running = True # 用于控制线程的启停
    
    def terminate(self):
        self._running = False # 停止该线程
        print("我被停止了")
    
    def run(self,n):
        # 注:为了防止IO阻塞,导致无法轮询,因此可以设置超时循环?????
        while self._running:
            print(f"{n}s")
            n -= 1
            time.sleep(1)

c = mytask()
p = Thread(target=c.run,args=(10,))
p.start()
time.sleep(3)
c.terminate()  
time.sleep(2)  # 子线程会在主线程结束后才会停止