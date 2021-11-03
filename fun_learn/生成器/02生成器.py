# 迭代器1
def generator():
    print("第一次")
    yield 1 # 运行到这里,将yield后面的值,作为该次__next__()的返回值
    print("第二次")
    yield 2 # 
    print("第三次")
    yield 3
g = generator()
res1 = g.__next__()
print(res1)
res2 = g.__next__()
print(res2)
res3 = g.__next__()
print(res3)
# 再多调用一次__next__()方法,就会抛出Stop的异常
res4 = g.__next__()

