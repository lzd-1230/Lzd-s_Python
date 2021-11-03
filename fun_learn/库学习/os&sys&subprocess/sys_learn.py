import sys
import time
# 拿到命令行给的参数
print(sys.argv) # 以列表的形式返回
"""打印进度条!!!!"""
# 1.格式化输出

def progess(cur_size,total):
    persent = cur_size/total # 计算百分比
    res = int(50*persent) * "#" # 打印#的长度
    print("\r[%-50s] %d%%" %(res,100*persent),end="") 


recv_size = 0
total_size = 200000
while recv_size < total_size:
    time.sleep(0.01)
    if(total_size - recv_size > 1024):
        recv_size += 1024
    else:
        recv_size += total_size - recv_size
    # 打印进度条
    progess(recv_size,total_size)
