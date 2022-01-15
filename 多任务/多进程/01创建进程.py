"""
windows下创建进程一定要在if __name__ == "__main__"函数下
    因为在win下相当于导入一个模块一样,逐行扫描你这个文件
    如果你创建进程的代码不在main中,则扫描的时候也会扫描到就会无线递归

Linux下则不需要,他会完完全全拷贝一份,然后直接再运行一遍
"""

from multiprocessing import Process
import time 

def task(name):
    print("%s is running" %name)
    time.sleep(1)
    print("%s is over" %name)


# 创建进程的方式一
# if __name__ == "__main__":
#     # 实例化一个进程对象
#     p = Process(target=task, args=("lzd",))
#     # 开启进程
#     p.start() # 告诉操作系统帮你开启一个进程
#     print("不进行等待,主进程直接执行")

# 创建进程的方式二:通过继承Process类
class MyProcess(Process):
    def __init__(self,name):
        Process.__init__(self)
        self.name = name
    def run(self):
        print("hello %s" %self.name)
        time.sleep(1)
        print("over")

if __name__ == "__main__":
	for i
    p = MyProcess("lzd")
    p.start()
    print("主进程")


