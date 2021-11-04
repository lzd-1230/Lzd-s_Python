
a = [1,5,2,1,9,1,5,10] 
# print(set(a)) # 如果是直接调用set则无法做到保序

def dedup(items):
    seen = set() # 创建一个集合
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

# 小知识点,将生成器作为列表的参数可以直接将迭代的元素构造成列表
print(list(dedup(a)))
