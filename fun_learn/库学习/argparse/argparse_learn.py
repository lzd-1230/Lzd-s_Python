import argparse

parser = argparse.ArgumentParser(description='本程序需要在命令行传入参数') # 创建一个解析对象
# type是要传入的参数的数据类型  help是该参数的提示信息
parser.add_argument("-n",'--name',type=str, help='姓名',default="张三") # integers可以单独引用
parser.add_argument("-s","--socre",type=int,help="成绩",default=0)

# 接收参数法1:只接收定义了的参数
args = parser.parse_args() # 拿到参数字典
print(args)

# 接收参数法2:接收
know_args = parser.parse_known_args()
print(know_args)
