price = {
    "phone":1888,
    "fruit":5,
    "CPU": 1200,
    "chicken": 2000
}
# 字典生成式
dic = {key:val for key,val in price.items() if val > 1200}
print(dic)
