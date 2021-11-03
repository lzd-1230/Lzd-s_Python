"""1.打开文件式"""
# 使用open直接打开(t模式)
# f = open(r"./file_model/study/test.txt")
# f = open(r"F:\file_sum2.0\Python\MyPython\file_model\study\test.txt")
    # f是一个对象,占用的内存空间
    # 同时操作系统会打开一个文件,映射到硬盘上的对应空间
    # 默认的操作模式为read,

# 使用with(同时使用非t模式)
with open("./file_model/study/passwd.txt",mode="rb") as f1:
    res1 = f1.read().decode("utf-8")
    print(res1)

"""2. 读/写文件"""
# r模式
# 文件不存在的时候报错
# 文件存在时文件指针跳到开始位置

# 应用程序对文件的独写,都是通过系统调用把输入输出读入内存,或者写入硬盘
# res = f.read()
# print(res)
# f.close() # 回收操作系统资源
# f还存在吗?在,但是已经不能再read了