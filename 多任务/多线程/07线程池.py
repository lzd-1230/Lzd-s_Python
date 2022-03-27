from concurrent.futures import ThreadPoolExecutor
import time

pool = ThreadPoolExecutor(3) # 只允许线程池中有3个任务同时进行

def task(n):
    print(n)
    time.sleep(2)
    return n**2

def call_backer(future):
    """
    回调函数:
        接收异步任务返回的future对象,可以调用result方法获取返回值
    """
    print("结果为:",future.result())

if __name__ == "__main__":
    for i in range(10):
        # 异步提交任务,并且添加回调机制
        pool.submit(task,i).add_done_callback(call_backer) 
    # 因为获取异步的结果会阻塞,因此这里需要放在后面再获取
    print("---------------------------------")
  