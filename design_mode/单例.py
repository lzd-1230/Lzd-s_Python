# 单例：即单个实例，指的是同一个类实例化多次的结果指向同一个对象，用于节省内存空间

HOST='1.1.1.1'
PORT=3306

def singo_obj(cls):
    __instance = cls(HOST,PORT)  # 这个就是生成的单例对象
    def wrapper(*args,**kwargs):
        if args or kwargs:
            res = cls(*args,**kwargs)
            return res
    return wrapper


#方式一:定义一个类方法实现单例模式
@singo_obj
class Mysql():
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port

obj1 = Mysql()
obj2 = Mysql()
print(obj1 is obj2)