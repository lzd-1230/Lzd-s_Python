import sys
import os 
"""
通过命令行拿到参数完成文件拷贝的功能
    当前实现:
        dst可以是路径
    未实现:
        src是一个目录
"""
try:
    src_path = sys.argv[1] # 拿到第一个命令行参数
    dst_path = sys.argv[2]
except Exception:
    print("请输入正确的参数形式<src> <dst>")

if(os.path.isdir(dst_path)):
    filename = os.path.basename(src_path)
    dst_path = os.path.join(dst_path,filename)

with open(src_path,mode="rb") as read_f,\
     open(dst_path,mode="ab") as write_f:

    while True:
        data = read_f.read(1024)
        if(not data):
            break
        write_f.write(data)
    