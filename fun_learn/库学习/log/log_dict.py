import os
import logging.config
"""
本文件用于配置日志格式：
    Filter：过滤日志的对象
    Handler：接收日志然后输出到不同的地方，FileHandler用来打印到文件中，StreamHandler用来打印到终端
    Formatter对象：可以定制不同的日志格式对象，然后绑定给不同的Handler对象使用，以此来控制不同的Handler的日志格式
    loggers:日志的产生者,最终在使用时只需要用它即可
        上述三种键值下一层的键值为自定义的形式
        比如:我在Formatter下定义了一个test形式,以后如果有日志想用这种格式,就使用test作为标识
"""


standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][日志名:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字
simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

logfile_dir = os.path.dirname(os.path.abspath(__file__))  # log文件的目录

logfile_name = 'MYLOG.log'  # log文件名

# 如果不存在定义的日志目录就创建一个
if not os.path.isdir(logfile_dir):
    os.mkdir(logfile_dir)

# log文件的全路径
logfile_path = os.path.join(logfile_dir, logfile_name)

LOGGING_DIC = {
    "version": 1,
    # 日志的输出格式
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    # 过滤器
    'filters': {},
    # 日志的接受流
    'handlers': {
        #打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    # 日志的不同种类:使用的时候只需要调这个key下的值即可。
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        "to_console": {
            'handlers': ['console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': False,  # 向上（更高level的logger）传递
        },
        "to_file":{
            "handlers": ["file"],
            "level": "WARNING",
            "propagate": False,
        }
        # 默认日志，大多时候直接调用时起名字即可
        "":{
            "handlers": ["file"],
            "level": "WARNING",
            "propagate": False,
        }
    },
}

def load_my_logging_cfg():
    logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
    logger = logging.getLogger(__name__)  # 生成一个log实例
    logger.info('It works!')  # 记录该文件的运行状态

if __name__ == "__main__":
    load_my_logging_cfg()