"""
管理员接口
"""
from db import db_header
from db import modules

admin_online = {
    "login":None
}

def admin_register(usr_name,passwd):
    # 判断用户名是否 # db_header.select(usr_name)存在 
    db_header.select_data(usr_name,"Admin")
    # 不存在,则创建
    admin = modules.Admin(usr_name,passwd)
    admin.save()

def query_own_info(usr_name):
    # 去查找该用户的文件是否存在
    flg,res_obj = db_header.select_data(usr_name,"Admin")
    
    if flg:    
        print("*********查询结果*********")
        print(f"管理员{usr_name}密码为{res_obj.passwd}")
    else:
        print(f"查询不到管里员{usr_name}")

def login_interface(usr_name,passwd):
    # 首先判断是否存在
    flg,res_obj = db_header.select_data(usr_name,"Admin")

    if flg:
        if passwd == res_obj.passwd:
            print(f"{usr_name}管理员登录成功!")
            admin_online["login"] = usr_name # 将状态添加到全局变量中
        else:
            print("密码输入错误")
    else:
        print("****用户不存在****")


def logout_interface():
    if admin_online["login"]:
        tmp = admin_online["login"]
        admin_online["login"] = None
        print(f"***账号{tmp}已经成功退出登录***")
        

