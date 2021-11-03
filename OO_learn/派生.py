class Person():
    def __init__(self,name,height,weight,):
        self.__name = name
        self.height = height
        self.weight = weight

"""重用方法一:直接调用(不继承也可以)"""
# class Student(Person):
#     # 重写了父类的方法
#     def __init__(self,namne,height,weight,score):
#         # 但是又有一部分和父类重复,因此重用一下
#         Person.__init__(name,height,weight)
#         # 自己重写的部分
#         self.score = score

"""重用方式二:使用super类进行调用,依照MOR顺序进行方法的查找"""
class Student(Person):
    def __init__(self,name,height,weight,score):
        # 调用方式二
        super().__init__(name,height,weight) # 调用的是绑定方法,自动传入self
        # 自己重写的部分
        self.score = score

s1 = Student("lzd","108","120","90")
print(s1.score)


"""
注意:派生是严格按照发起者的MRO顺序去进行方法的查找的
"""

class A():
    def test(self):
        # print(A.mro())
        super().test() # 这里根本找不到,最终为空
class B():
    def test(self):
        print("我是B的test")

class C(A,B):
    def __init__(self):
        super().test()

c = C()
print(C.mro()) 

"""
有点问题呐,为啥我现在找到A的test方法后,还会继续去找B的啊?
"""