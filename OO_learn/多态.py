
class Animal():
    # 一个接口,动物都可以去重写的功能
    def scream():
        pass

class Dog(Animal): 
    def scream(self): # 注意这里一定要写self来区分这个是你这个对象的方法
        print("Dog scream")

class Cat(Animal):
    def scream(self):
        print("Cat scream")

# 实现了一个全局调用的方法,传入不同的对象,得到不同的函数调用
def Talk(animal):
    animal.scream()

cat = Cat()
dog = Dog()

cat.scream()
dog.scream()
Talk(cat)
Talk(dog)

"""
起始多态在python中应用太广泛了
    为什么我们len(列表),len(字典),len(元组)都可以??
        因为本质上python在这些类中都内置了一个__len__()方法
    for循环为啥可以for那么多个类??
        因为它们这些类都内置了__iter__()
"""
