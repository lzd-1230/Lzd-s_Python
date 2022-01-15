from threading import Semaphore,Thread
import random
import time

def fun(name):
    s.acquire()
    print(f"{name}正在蹲坑")
    time.sleep(random.randint(1, 3))
    s.release()

s = Semaphore(3)

if __name__ == "__main__":
    for i in range(15):
        p = Thread(target=fun, args=(f"{i}号", ))
        p.start()