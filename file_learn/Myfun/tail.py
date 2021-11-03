"""
实现命令行终端的tail -_f 功能
还有bug:
    最终输出行数不匹配
    如果日志内容过大没有测试过

"""
import time
import sys  

class Tail():
    def __init__(self,path):
        self.path = path

    def is_exist(self):
        try:
            self._f = open(self.path,mode="r") # 以rb方式打开
            self.file_len = self._f.tell()

        except Exception as e:
            print("请输入正确的文件路径")
            # print(e)

    def follow(self):
        # 判断文件是否存在
        self.is_exist()

        self._f.seek(0,2) # 指针跳到函数最后
        while True:
            line = self._f.readline()
            if(line):
                # print(line.decode("utf-8"),end="")
                sys.stdout.write(line)
                # 还可以进行扩展,比如显示在浏览器上
    
    def show_last_n(self,n = 10):
        self.is_exist()
        last_read = []
        read_len = 100*n

        while True:
            # 当前还没10行,直接全部读完
            if read_len > self.file_len:
                self._f.seek(0) 
                last_read = self._f.read().split("\n")[-n:] # 选取最后n行
                break
            # 如果文件内容大于1000个字符
            self._f.seek(-read_len,2) # 取倒数
            # 数出换行符的数量
            last_read = self._f.readlines()
            count = last_read.count("\n")
            print(count)
            # 如果读出指定内容大于n行,则选取最后n行即可
            if count >= n:
                last_read = last_read[-n:]
                break
            # 换行符不够n行
            else:
                print("换行符不够")
        for line in last_read:
            print(line)

    def close(self):
        self._f.close()

path = input("请输入要跟踪的文件路径:")
t = Tail(path)
t.show_last_n(10)
t.close()