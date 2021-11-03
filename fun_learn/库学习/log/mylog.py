"""
日志模块的使用
"""
# 让logging模块加载我们的字典配置
import log_dict
from logging import config,getLogger  # 或者import logging.config as config
# 导入配置字典
config.dictConfig(log_dict.LOGGING_DIC)
# 拿到日志的产生者
my_logger = getLogger("to_file")

my_logger.warning("日志测试")