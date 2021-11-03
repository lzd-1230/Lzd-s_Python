# 函数名==函数指针
fun_dict = dict()

def add(*args):
    tmp = 0
    for i in args:
        tmp+=i
    return tmp

fun_dict["add"] = add
print(fun_dict["add"](1,2,3))

# 函数名可以作为函数参数
def foo(x,y,foo):
    return foo(x,y)
print(foo(1,2,add))