import hashlib
"""
hash库调用方法
"""
m = hashlib.md5()  # 创建一个hash工厂
# 可以一点一点地把内容update进去,类比可以把文件一点一点地传进
m.update("hello".encode("utf-8"))
m.update("world".encode("utf-8"))  # 必须encode成byte类型才能够hash
res = m.hexdigest()
print(res)

"""真实猜密码模拟"""
# 网上有很多地密码字典,可以拿过来一个个猜
# 对策:密码撒盐,进行一定规则的修改,将密码改地面目全非   

guess = ["ggg123","123ggg","1ggg23","gg123g"]
guess_dict = dict()
true_kw = hashlib.md5("123ggg".encode("utf-8")).hexdigest() # md5加密

for passwd in guess:
    guess_dict[passwd] = hashlib.md5(passwd.encode("utf-8")).hexdigest() # 猜一个md5出来

for key,val in guess_dict.items():
    if(val == true_kw):
        print("找到了密码:",key)
    

# 但是真实的文件如果太大了的话,这个方法太慢了!
# 因此真实地场景往往是随机取点小段小段地校验,而不是全部扔进去校验

