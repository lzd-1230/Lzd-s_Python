# 第一次导入这个包的时候(任何方式,from 或者直接import),init就会被执行一次
# 绝对导入
import package_learn.Afun.foo as Afun # 现在你的包里面就有一个叫Afun的模块了!
import package_learn.Bfun.foo as Bfun
print("__init__")
import sys # 第三方包的依赖
# 相对导入
from .test import * # test模块中的所有函数都可以被外面用from import的方式来导入了!