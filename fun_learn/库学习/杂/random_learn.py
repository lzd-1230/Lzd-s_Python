import random

# 0-1的浮点数
print(random.random())

# 闭区间内的小数[a,b]
print(random.uniform(1,3))

# [1,3]之间的整数
print(random.randint(1,3))
# 左闭右开的整数[1,3)
print(random.randrange(1,3))

# 从列表中随机抽取
print(random.choice([1,2,3,"lzd"]))

# 从列表中随机组合n个东西出来
n = 2
print(random.sample(["lzd","wy","lzr"],n))

# 洗牌
l = [1,3,4,5,6,7]
random.shuffle(l) # 直接对原列表进行修改
print(l)

"""随机验证码"""
# 成语类型的
l = ["嘿","离","谱"]
res = random.sample(l,3)
print(res)
# 从26个字母中选一个
res = ""
for i in range(4):
    tmp_big = chr(random.randint(65,90)) # 大写字母
    tmp_small = chr(random.randint(97,122))
    tmp = random.choice([tmp_small,tmp_big])
    res+=tmp
print(res)
