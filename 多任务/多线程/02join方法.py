import time
import threading

value = 0

def thread_body(name):
    global value 
    print(f"{name} 开始")
    for n in range(3):
        print(f"{name} 执行")
        value += 1
        time.sleep(1)

print("主线程开始")
t1 = threading.Thread(target=thread_body,args = ("Thread A",),name="Thread A")
t1.start()
t2 = threading.Thread(target=thread_body,args=("Thread B",),name="Thread B")
t2.start()
# 主线程等待 t1 运行完毕
t1.join()
print(f"value = {value}")
print("主线程结束")