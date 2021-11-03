"""位置参数在左边,默认参数在右边"""
def register(name,sex,age):
    print(f"name={name} sex={sex} age={age}")

register(18,"男",age=20) # 注意关键词参数一定要放在后面

"""默认参数只能是不可变的"""
def foo(n,arg=[]):    
     arg.append(n)    
     return arg    
foo(1)    
foo(2)    
print(foo(3)) # 如果设置成可变的话,就会有记忆特点,不符合要求

"""溢出参数"""
def add(*args):
    Sum = 0
    for i in args:
        Sum += i
    return Sum 
print(add(1,2,3,4))

"""可变长关键字参数 keyword args"""
def show_val(**kwargs):
    print(kwargs)
show_val(x=2,y=3,z=4)

"""从某一个变量开始之后为关键字参数"""
def forec_key(x,y,*,z):
    print(f"x:{x} y:{y} z:{z}")
forec_key(1,2,z=3) # 最后一个参数必须时命名参数

"""在函数内部将参数传递给另一个参数"""
def other_fun(*args,**kwargs):
    pass
def pass_args(*args,**kwargs):
    other_fun(*args,**kwargs) # 使用元组和字典的解包

pass_args(4,z=5,k=6)

# **kwargs在作为形式参数时表示任意个关键词参数
# **kwargs在作为实参时表示将字典解包成key=value的格式传入(仅在作为实参的时候有用)
