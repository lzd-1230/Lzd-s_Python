from core import admin
from interface import admin_interface


def auth(obj_name):
    def login_wrapper(func):
        def call_func(*args,**kwargs):
            res = None
            # 判断用户是否已经登录过了
            if obj_name == "Admin":
                if admin_interface.admin_online["login"]:
                    res = func(*args,**kwargs)
                else:
                    print("***要完成该功能请先进行登录***")
                    admin.login()
            elif obj_name == "Student":
                pass
            
            else:
                print("该类型用户没有权限")
            return res 
        return call_func
    return login_wrapper