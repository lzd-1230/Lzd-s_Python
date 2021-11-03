"""
当内嵌函数包含对外部函数作用域中变量的引用,那么该内嵌函数称为闭包。
"""
x=1
def outer():
    x = 3
    def inner():
        print(x)
    return inner

func=outer()
func() # 结果为2,因为该函数为闭包
print("------包裹的外部变量--------")
print(func.__closure__[0].cell_contents)
