"""
生成器的构成部分
	可以再外面用next()函数,把生成器作为参数传入
	
yield:程序的挂起->并发编程

"""
import random
def dog():
    print("数据处理携程已经准备完毕")
    while True:
        x = yield 1230 # 先返回再说,等会再回来
        print(f"原始数据处理结果为{x**2}")

g = dog()
res = g.send(None) # 如果不send回来,x的值就是1230
print(res)

a = random.randint(1,5)
res = g.send(a)
print(res)