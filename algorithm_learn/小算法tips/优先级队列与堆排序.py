import heapq
"""
基础找最大最小的n个值
"""
nums = [1,3,-2,4,9,-10,23]

mins_3 = heapq.nsmallest(3,nums) # 找到最小的3个
maxs_3 = heapq.nlargest(3,nums)
# print(mins_3)

"""
优先级队列:
    1.优先返回最高优先级的元素
    2.多个最高优先级则按照队列顺序出队
实现原理:
    利用堆数据结构+元组的特点,按照元组中前两位(优先级,插入顺序)的值依次进行排序
"""
class PriorityQueue():
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item)) # 你传进去一个元组,则会默认从第一个位置的元素开始比较,如果第一个元素位置相同,再到第二个元素
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1] 
que = PriorityQueue()
que.push("foo",1)
que.push("bar",5) # 优先级最高
que.push("spam",4)
que.push("grok",1)

print(que.pop())
print(que.pop())
print(que.pop())
print(que.pop())
# print(que.pop()) # 多pop则报错

