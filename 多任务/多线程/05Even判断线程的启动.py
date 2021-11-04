from threading import Thread,Event
import time

def countdown(n, stared_evt):
    """
    stared_evt: 传入了一个Event对象给它,这样他就能够知道自己什么时候执行
        然后使用Event.wait(),直到它阻塞结束后代表线程开始执行
    """
    print("count down starting")
    stared_evt.set()
    while n>0:
        print(f"{n}-minus")
        n -= 1
        time.sleep(2)

started_evt = Event() # 创建一个Event对象

t = Thread(target=countdown, args=(10,started_evt,))
t.start()

started_evt.wait() # 主线程等待子线程中执行完 stared_evt.set() 之后再执行
print("task is running")