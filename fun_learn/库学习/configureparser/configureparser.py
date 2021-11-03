"""
这是一个读取配置文件的库
"""

import configparser as cfg

config = cfg.ConfigParser()
config.read("./fun_learn/第三方库学习/test.ini")
# print(config.sections()) # 拿到所有的块标题

# 查看标题下所有标题为route的key(options)
options = config.options("route")
# print(options)

# 查看标题下所有标题为route的item(key-value)
items = config.items("route")
# print(items)

# 查看某一个section下某一个key的value 
val = config.get("route","tar")
print(val)

# 判断配置文件下是否含有标题
print(config.has_section("route"))
# 判断标题下是否含有某option
print(config.has_option("route","tar"))

# 增
config.add_section("lzd") # 增加一个section
config.set("lzd","name","LZD_1230") # 在section下增加option并设置value
config.write(open("./fun_learn/第三方库学习/test.ini","w"))

# 删的内容还是不要乱用了....