
my_list = [1,3,5,6,8,10,21,31]

def my_fliter(val):
    """
    该函数接收列表中的元素,返回一个bool,表示这个元素是否要被筛选进入生成器
    """
    if(val %2 ==0):
        return True
    else:
        return False
    
my_gen = filter(my_fliter,my_list)
# print(list(my_gen))

"""
插曲:利用bool列表进行切片筛选
"""
from itertools import compress
bool_index = [True if x%2 ==0 else False for x in my_list]
# print(bool_index)
print(list(compress(my_list, bool_index)))