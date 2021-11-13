from multiprocessing import current_process,Process
import time
import os


def task():
    # print(f"{current_process().pid} is running")
    print(f"{os.getpid()} is running")
    time.sleep(2)

if __name__ == "__main__":
    p = Process(target=task)
    p.start()
    p.join()
    print(f"主进程{current_process().pid} over")