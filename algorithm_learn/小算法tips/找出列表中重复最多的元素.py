from collections import Counter

List = ["a","a","a","b","b","c"]

char_counts = Counter(List)
top_two = char_counts.most_common(2)
# print(top_two) # [('a', 3), ('b', 2)]
# print(char_counts) # 其本质上是一个字典的结构! Counter({'a': 3, 'b': 2, 'c': 1})

"""
Counter对象可以动态地添加元素
"""
List_add = ["b","b","d","c"]
char_counts.update(List_add)
# print(char_counts.most_common(2)) # [('b', 4), ('a', 3)]

"""
同时多个Counter对象可以进行加减运算,即对应元素出现的次数相加减
"""
