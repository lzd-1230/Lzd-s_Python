"""
property就是一个装饰器:
    具体的类实现装饰器的功能暂时不用了解,后续可以查看egon博客描述符那一块
作用一:
    1.某些功能是通过计算得到的,因此必须是一个方法
    2.调用时只显示一个数据的属性,而不是一个函数
封装思想的衍生,本质上就是将方法化妆成属性

作用二:
    对私有属性的读取,修改,删除
"""

class Person():
    def __init__(self,name,height,weight,):
        self.__name = name
        self.height = height
        self.weight = weight
    @property
    def BMI(self):
        return self.weight / (self.height**2)

    @property # 这一步之后,name也变成一个装饰器了
    def name(self): # 下面三个函数名都对应着用户想访问的属性
        return self.__name
    @name.setter # 固定用法
    def name(self,val):
        self.__name = val
    @name.deleter
    def name(self):
        print("不许删除")

me = Person("lzd",1.82,62.5)
print(me.BMI)
print(me.name)
me.name = "lzd1230"
print(me.name)
del me.name

