import time

def test():
    time.sleep(1)

def count_time(func):
    def set_fun():
        start_time = time.time()
        res = func()
        end_time = time.time()
        print(f"函数的运行时间:{round(end_time - start_time,2)}")
        return res # 原来函数的执行结果不能改变
    return set_fun 
# 无参装饰器的实现原理,函数指针的替换!
test = count_time(test)
test()
# 如果用装饰器语法就是
@count_time # 语法糖:test = count_time(test),因此叠加多个也无非就是串联赋值而已
def test():
    time.sleep(1)
test()

# 无参装饰器模板
def outter(func):
    def wrapper(*args,**kwargs):
        # 执行函数前的添加的操作
        res = func(*args,**kwargs)
        # 执行函数后拓展的操作
        return res
    return wrapper # 这一步return是为了将wrapper返还给全局区


"""
那如果要求装饰器有参数怎么办?
    装饰器有参数->再加一层闭包给参数
"""
def set_wrapper(val): # 这一层的参数可以任意加
    def wrapper(func):
        def call_fun(*args,**kwargs):
            if(val == 1):
                print("---一级验证---")
            elif(val == 2):
                print("---二级验证---")
            res = func(*args,**kwargs)
            return res 
        return call_fun
    return wrapper

@set_wrapper(2) # 核心原理:  wrapper = set_wrapper(val) func = wrapper(*args,**kwargs)
def fun(x,y):
    print(f"x={x} y={y}")

fun(1,2)

"""多装饰器的顺序"""

def outer1(x,y):
    def wrapper1(func):
        def call_func(*args,**kwargs):
            print(f"装饰器1:{x},{y}")
            res = func(*args,**kwargs)
        return call_func
    return wrapper1

def outer2(x,y):
    def wrapper2(func):
        def call_func(*args,**kwargs):
            print(f"装饰器2:{x},{y}")
            res = func(*args,**kwargs)
        return call_func
    return wrapper2

@outer2(2,2)
@outer1(1,1)
def test():
    print("原函数功能")

test()