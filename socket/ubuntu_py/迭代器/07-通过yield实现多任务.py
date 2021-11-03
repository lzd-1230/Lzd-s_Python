import time
"""
通过yield使得函数进行挂起,只有当下一次调用next时,才会继续调用.
"""

def task1():
    while True:
        print("----1-----")
        yield  # next调用一次走一遍
        time.sleep(0.5)
    
def task2():
    while True:
        print("---2----")
        yield
        time.sleep(0.2)


def main():
    t1 = task1()
    t2 = task2()
    while True:
        next(t1)
        next(t2) 

if __name__ == "__main__":
    main()
