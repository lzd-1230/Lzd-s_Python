import copy
import random

# 判断算法返回结果是否相等
def is_equle(res1,res2):
    pass

# 首先生成一个随机长度的随机数组
def get_random_array(length,N_max):
    if(length<1):
        print("长度输入太短")
        return None
    
    arr = [(int)(random.random()*N_max) for i in range(length)]
    return arr

# 进行多次测试
def test(count):
    for i in range(count):
        arr = get_random_array(100,100) # 拿到一定长度一定范围的数组
        arr1 = copy.deepcopy(arr)
        arr2 = copy.deepcopy(arr)
        # -----执行两种算法,一种标准的,一种你自己不确定的
        res1 = fun1(arr1)
        res2 = fun2(arr2)
        if(not is_euqle(res1,res2)):
            print("----测试失败----")
            print(f"fun1的输出结果为{res1}")
            print(f"fun2的输出结果为{res2}")
            print(f"测试用例为{arr}")

            