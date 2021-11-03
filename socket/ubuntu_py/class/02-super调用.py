class Parent():
    def __init__(self,name):
        print("--Parent的init开始被调用--")
        self.name = name 
        print("--Parent的init调用完成--")

class Son1(Parent):
    def __init__(self,name,age,*args,**kwargs):
        print("--Son1的init开始被调用--")
        self.age = age
        Parent.__init__(self,name)
        print("--Son1的init调用结束--")

class Son2(Parent):
    def __init__(self,name,gender,*args,**kwargs):
        print("--Son2的init开始被调用--")
        self.gender = gender 
        Parent.__init__(self,name)
        print("--Son2的init调用结束--")

# 这时候上面有3个init,到底调用谁的?
class Grandson(Son1,Son2):
    def __init__(self,name,age,gender):
        print("--Grandson的init开始被调用--")
        super(Grandson,self).__init__(name,gender)
        print("--Grandson的init调用结束--")

gs = Grandson("grandson",18,"man")
print("name:",gs.name)
print("gender:",gs.gender)
print("age:",gs.age)
print("调用顺序:",Grandson.__mro__)
print("调用顺序:",Son1.__mro__)
