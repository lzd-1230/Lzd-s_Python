"""
堆(最小堆)就是一个 父节点val>=子节点val的二叉树
那么堆的根节点一定是整颗二叉树中最小的元素
堆排序是一个不稳定的排序,而python自带的sorted方法是稳定的
"""
import heapq

def heapsort(iterable):
    h = []
    for i in iterable:
        heapq.heappush(h,i)
    return [heapq.heappop(h) for i in range(len(h))]

a = [1,3,4,2,6,8,2]
b = heapsort(a)
# print(b)

"""
注意:堆排序中元素可以是元组,这样则会让比较任务的优先级变得很方便
"""
