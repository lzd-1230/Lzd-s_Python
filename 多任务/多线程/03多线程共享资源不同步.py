"""
本程序模拟飞机票出售系统中的进程不同步的问题
    问题的根本:读写同一个变量在汇编级别并不是原子的,不同的线程可能读取的是上一个线程操作过的旧数据

    解决方法:
        上锁:只有拿到锁的线程才会开始执行,没拿到的就只能乖乖交出CPU占用权
            如果上锁的方式不对,则效率巨低,甚至有违并发的初衷
            多个锁并且上锁解锁顺序不对很可能造成死锁
"""
import threading
import time

class TicketDB():
    def __init__(self):
        self._ticket_num = 5
    def get_ticket_num(self):
        return self._ticket_num
    
    def sell_ticket(self):
        # 睡眠1s模拟用户付款状态
        time.sleep(1)
        print(f"第{self._ticket_num}号机票已经出售")
        self._ticket_num -= 1 # 其中的问题就出现在这里了

def thread_body():
    global db
    lock.acquire()
    while True:
        cur_ticket = db.get_ticket_num()
        if cur_ticket > 0:
            db.sell_ticket()
        else:
            break
    lock.release()
    time.sleep(1)

db = TicketDB()
lock = threading.Lock()

t1 = threading.Thread(target=thread_body)
t1.start()
t2 = threading.Thread(target=thread_body)
t2.start()

