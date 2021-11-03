from collections import defaultdict
from collections import OrderedDict

"""多值字典(列表字典)"""
d = defaultdict(list) # 会给每一个key初始化成空列表
d["a"].append(1)
d["a"].append(2)
d["b"].append(4)
# print(d["a"])
# print(d["b"])

"""有序列表:如果想在序列化后精确控制键值的顺序,则只要使用这个数据结构即可,但是空间成本会高一倍"""
d = OrderedDict()
d["foo"] = 1
d["bar"] = 2
d["span"] = 3

# for key in d:
#     print(key,d[key])

"""与字典键-值计算的问题"""
# 将key-val倒置
d = dict()
d["foo"] = 1
d["bar"] = 2
d["span"] = 3
d_val_key = zip(d.values(),d.keys()) # 以元组的形式组合起来,让val在前面作为排序的依据
# print(max(d_val_key))

# 直接指定键值,对进行排序,最后以key的形式进行返回
x = sorted(d,key=lambda k: d[k],reverse=True)
# print(x)

"""字典键值的集合操作"""
a = {
    "x": 1,
    "y": 2,
    "Z": 3,
}
b= {
    "w":10,
    "x":9,
    "y":2,
}

# 转化成keys类型后
print(a.keys() & b.keys()) # 两个dict_keys类型的 &操作返回的是交集
# 转化成items类型后
print(a.items() & b.items()) # 两个一模一样的item
