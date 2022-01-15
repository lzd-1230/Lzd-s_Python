from concurrent.futures import ThreadPoolExecutor
pool = ThreadPoolExecutor(3) # n不指定会自动帮你指定
import time

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
    t_list = []
    for i in range(10):
        # 异步提交任务,并且添加回调机制
        res = pool.submit(task,i).add_done_callback(call_backer) 
        # t_list.append(res)

    # -----不太优雅的获取结果方式-------
    # 关闭线程池,不让别的服务进入,并且等待线程池运行完毕(都拿到了结果),这种方法不好
    # pool.shutdown()

    # 因为获取异步的结果会阻塞,因此这里需要放在后面再获取
    # for t in t_list:
    #     res = t.result()
    #     print("结果为:",res)