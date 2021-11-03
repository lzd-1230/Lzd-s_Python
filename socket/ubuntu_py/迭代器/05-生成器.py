"""
生成器的基本原理:

"""
def Generater():
    a = 0
    b = 1
    i = 0
    cnt = 10
    print("-----1------")
    while i < cnt:
        print("-----3------")
        yield a  # 每一次经过这里都会将值返回一次
        print("-----2------")
        a, b = b, a+b
        i += 1

gen = Generater() # 这里只会构建好生成器但并不会执行,因为yield的限制,只有当第一次next调用后才会
"""用next调用 """
# ret = next(gen) # 这一次调用
# print(ret)
# ret = next(gen)
# print(ret)


"""直接用for调用"""
# for num in gen:
#    print(num)
