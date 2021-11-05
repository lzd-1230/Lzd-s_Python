"""
相同其语法与线程模块基本
"""
import time
import math	
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

PRIME = [112272535095293] * 10 # 检查100个素数

def is_prime(n):
    if n<2:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))

    for i in range(3, sqrt_n+1,2):
        if n%i == 0:
            return False
    return True

def task():
    for n in PRIME:
        is_prime(n)

def multi_thread_task():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, PRIME)

def multi_process_task():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime, PRIME)
    
if __name__ == "__main__":
    start = time.time()
    task()
    end = time.time()
    print(f"单线程耗时{end-start}s")

    start = time.time()
    multi_thread_task()
    end = time.time()
    print(f"多线程耗时{end-start}s")

    start = time.time()
    multi_process_task()
    end = time.time()
    print(f"多进程耗时{end-start}s")
