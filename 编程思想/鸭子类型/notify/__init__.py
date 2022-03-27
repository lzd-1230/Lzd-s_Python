import settings
import importlib

def send_all(content):
    for way in settings.NOTIFY_WAYS:
        model_path,cls_path = way.rsplit(".",maxsplit=1)
        # 利用importlib来获取模块
        model = importlib.import_module(model_path)
        # 利用反射来获取方法名称
        my_class = getattr(model,cls_path)
        obj = my_class(content)
        # 利用鸭子类型调用send方法
        obj.send()
