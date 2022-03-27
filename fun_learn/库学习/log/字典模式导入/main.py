import settings
import logging.config # 注意logging中的__init__.py文件中没有config,因此要显示地导入子包


logging.config.dictConfig(settings.LOGGING_DIC)
loger_test = logging.getLogger("second_logger")
loger_test.error("测试logger")




