"""
一个复制的小案例程序
"""

path_origin = input("请输入源文件绝对路径")
path_dst = input("清输入目标文件路径")

with open(path_origin,"rb") as f_ori:
    f_dst = open(path_dst,"ab")
    while(True):
        data = f_ori.read(1024) # 每次读1024Bytes
        if(len(data) == 0):
            break
        f_dst.write(data)
        