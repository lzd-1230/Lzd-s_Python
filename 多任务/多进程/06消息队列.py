from multiprocessing import Queue,Process
"""
使用模块自带的队列模块,其本质是管道subprocess+锁机制
    q = Queue()
常用方法
    q.full() # 判断队列是否满了
    q.get() # 从队头获取元素
        timeout参数:如果队列中没有元素,等待多少秒之后抛异常
    q.put() # 从队尾添加元素 
IPC进程间通信:
    主进程和子进程进行通信
    子进程之间进行通信
"""
def task1(q):
    q.put(11)
    print("task 1 over")

def task2(q):
    print("wait for que")
    print(q.get())

if __name__ == "__main__":
    q = Queue() # 注意队列一定要作为参数传递给进程函数才可以
    p1 = Process(target=task1,args=(q,))
    p2 = Process(target=task2, args=(q,))
    p1.start()
    p2.start()
