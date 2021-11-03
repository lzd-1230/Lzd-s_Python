# lambda函数用于快速完成某一功能的匿名函数编写 

salaries={
    'siry':3000,
    'tom':7000,
    'lili':10000,
    'jack':2000
}
res = sorted(salaries,key=lambda k:salaries[k]) # 迭代出来的是薪资,这里的k是salaries迭代出来的元素
print(res)