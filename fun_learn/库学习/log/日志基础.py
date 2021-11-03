import logging
"""
日志的配置主要为了实现:
    1.如何控制日志既输入到文件,也显示到终端
    2.如何控制写入文件时的编码
日志名：一定要细化，最好是通过日志名大概就能够看出是什么模块的问题
日志轮转：
    日志太大了大都打不开，因此要定期进行分割
    
"""

logging.basicConfig(filename='access.log',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=30)


logging.debug("debug")  # 最低级别10
logging.info("info")    
# 默认的日志级别为30,因此只会输出以上的
logging.warning("警告warn") # pandas中那个索引问题就老报这个级别的 30
logging.error("错误") 
logging.critical("严重错误") # 最高级别 50 
