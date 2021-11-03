import multiprocessing

n = 100

def fun():
    global n
    n = 0
    print("son_process",n)

if __name__ == "__main__":
    p = multiprocessing.Process(target=fun)
    p.start()
    p.join()
    print("main_process",n) # 这一句会被先执行?????



