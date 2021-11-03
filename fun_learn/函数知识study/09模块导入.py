# coding=utf-8
from package_learn import sys
from package_learn.test import x
from package_learn import change
from package_learn import Afun

# foo.get() # 查看模块中全局变量x的值
"""在本函数中创建一个同名的全局变量"""
x = 1 # 在运行函数中创建一个同名变量把上面引用的x换了个指向
# foo.get() # 不会影响

"""调用修改函数修改一下"""
foo.change() 
foo.get() # 可以完全修改

Afun.foo1() # 
print(sys.path) # 存放了搜索的文件夹列表
# print(sys.modules)