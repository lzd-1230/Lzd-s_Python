import logging

"""
日志的配置主要为了实现:
    1.如何控制日志既输入到文件,也显示到终端
    2.如何控制写入文件时的编码
日志名：一定要细化，最好是通过日志名大概就能够看出是什么模块的问题
日志轮转：
    日志太大了大都打不开，因此要定期进行分割
    
"""

# 第一步，创建一个logger
logger = logging.getLogger("test_logger") # 这里可以传递一个名字
logger.setLevel(logging.DEBUG)  # Log等级总开关

# 第二步,创建一个handler用于写入文件,可以指定文件的写入类型
file_path = "./access.log"
file_handler = logging.FileHandler(file_path,mode="w",encoding="utf-8")
file_handler.setLevel(logging.INFO) # 这个级别只能大于总开关的级别

# 第三步,设置日志格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
file_handler.setFormatter(formatter)
# 第四步,将file_handler添加进logger中
logger.addHandler(file_handler)

# 如果既想往终端输入,又想往文件输入,则再创建一个往终端输入的handler
consle_handler = logging.StreamHandler()
consle_handler.setLevel(logging.DEBUG)
consle_handler.setFormatter(formatter)
# logger.addHandler(consle_handler)


# 真正使用时使用最开始定义的logger就可以,handler会在里面根据条件自己过滤输出的位置和内容
logger.debug("这是一个debug")  # 最低级别10
logger.info("info")    
# 默认的日志级别为30,因此只会输出以上的
logger.warning("警告warn") # pandas中那个索引问题就老报这个级别的 30
logger.error("错误") 
logger.critical("严重错误") # 最高级别 50 

# 记录在try中的错误
try:
    a =1/0
except Exception as e:
    logger.error("here raise an err",exc_info=False)
