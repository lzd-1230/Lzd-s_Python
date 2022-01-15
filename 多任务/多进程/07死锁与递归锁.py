from threading import Thread,Lock
import time

"""
注意这里要使用线程来实验,使用进程不会产生死锁现象??
"""
mutexA = Lock()
mutexB = Lock()

class Dead_Lock(Thread):
    def run(self):
        self.fun1()
        self.fun2()

    def fun1(self):
        mutexA.acquire()
        print(f"{self.name}抢到了A锁")
        mutexB.acquire()
        print(f"{self.name}抢到了B锁")
        mutexB.release()
        mutexA.release()
        print(f"{self.name}溜了")
    
    def fun2(self):
        mutexB.acquire()
        print(f"{self.name}抢到了B锁")
        time.sleep(2)
        mutexA.acquire()
        print(f"{self.name}抢到了A锁")
        mutexA.release()
        mutexB.release()

if __name__ == "__main__":
    for i in range(10):
        p = Dead_Lock()
        p.start()