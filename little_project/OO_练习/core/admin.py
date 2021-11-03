from interface import admin_interface
from lib import common

def admin_register():
    usr_name = input("请输入管理员用户名:")
    passwd = input("请输入管理员密码")
    re_passwd = input("请再次输入管理员密码")
    # 小逻辑判断后调用接口层
    if( passwd == re_passwd):
        # 调用接口层函数
        admin_interface.admin_register(usr_name,passwd)

        
    else:
        print("两次输入的密码不一致")
        return False

@common.auth("Admin")
def modify_score():
    pass

@common.auth("Admin")
def query_passwd():
    usr_name = input("请输入要查找的管理员姓名:")
    admin_interface.query_own_info(usr_name)


def login():
    usrname = input("请输入管理员用户名:")
    passwd = input("请输入管理员密码") 

    admin_interface.login_interface(usrname,passwd)

@common.auth("Admin")
def logout():
    choose = input("是否真的要退出当前账号?(y/n)")
    if choose == "y":
        admin_interface.logout_interface()
    else:
        pass


func_dict = {
    "1":admin_register,
    "2":modify_score,
    "3":query_passwd,
    "4":login,
    "5":logout,
}

def admin_view():
    while True:
        print(
            '''
            =====管理员面板======  
            1.管理员注册
            2.修改学生分数
            3.查询管理员信息
            4.管理员登录
            5.退出当前账号
            '''
        )
        choice = input("请输入功能:")
        
        if( choice not in func_dict ):
            print("功能输入错误,请重新输入")
            continue

        func_dict[choice]()

