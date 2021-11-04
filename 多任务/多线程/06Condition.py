"""
如果线程打算一直重复通知某一个事件,则可以使用Condition对象来处理
"""
import threading
import time

class Predictor():
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition() 
    
    def start(self):
        t = threading.Thread(target=self.run, daemon=True)
        t.start()
    
    def run(self):
        # 启动定时器,周期性地通知等待线程
        while True:
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all() # 通知所有等待的线程
    
    def wait(self):
        """
        wait for the next tick
        """
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait() # 等待定时器通知



ptimer =  Predictor(3)
ptimer.start()

def countdown(nticks):
    while nticks>0:
        ptimer.wait()
        print(f"{nticks}mins")
        nticks -= 1

def coutup(last):
    n = 0
    while n < last:
        ptimer.wait()
        print(f"Counting {last}")
        n+=1


threading.Thread(target=countdown, args=(10,)).start()
threading.Thread(target=coutup, args=(5,)).start()
