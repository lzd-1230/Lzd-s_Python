d = {"a":1,"b":2,"c":3} # 一个字典
a = iter(d) # 转换成迭代器,相当于多了一个__next__方法,其它不变.
# 如果少了上面那一句,则无法

while True:
    try:
        print(a.__next__())
    except StopIteration:
        break
# 这个时候并不会继续迭代,为啥呢?
    # 可能是现在的__next__方法已经指向异常了,因此就不能再迭代了
    # 因此如果需要多此使用的话,需要先将原来的迭代器删除,然后再创建一个
del a
a = iter(d)
for key in a:
    print(key)