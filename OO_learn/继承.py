"""
新式类问题:python3类所有的类都是新式类,因此可能不兼容python2
    因此默认构造类的时候还是加上(object)参数
    object类中有一些常用的方法

继承的作用:
    解决类和类之间功能重用的问题
"""
class Person():
    def __init__(self,name,height):
        self.name = name
        self.height = height

class Student(Person):
    def __init__(self,name,height,score):
        super().__init__(name,height)
        self.score = score

class Teacher(Person):
    def __init__(self,name,height,salary):
        super().__init__(name,height)
        self.salary = salary
     