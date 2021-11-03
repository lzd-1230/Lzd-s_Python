from conf.setting import * # 拿到所有的路径变量
import pickle
import os 

ADMIN_DB_PATH = os.path.join(
    DB_PATH,"Admin"
)

# 用于保存对象
def save_data(obj):
    cls_dir = os.path.join(
        DB_PATH,obj.__class__.__name__ # 该类的文件夹是否已经创建
    )
    # 如果没有创建目录的话需要先创建目录
    if(not os.path.exists(cls_dir)):
        os.mkdir(cls_dir)
    
    usr_path = os.path.join(
        cls_dir,obj.usr_name # 属于该用户的路径
    )
    
    with open(usr_path,mode="wb") as f:
        pickle.dump(obj,f)

# 根据类名和用户名来查看对象
def select_data(usr_name,cls_name):
    if (cls_name == "Admin"):
        if(not os.path.exists(ADMIN_DB_PATH)):
            print("目前还没有一个管理员用户,请先注册一个")
        usr_path = os.path.join(
            ADMIN_DB_PATH,usr_name
        )

        if(os.path.exists(usr_path)):
            with open(usr_path,mode="rb") as f:
                res_obj = pickle.load(f)
            return True,res_obj
        else:
            return False

# def select_data(usr_name,cls_name):
#     print("*********查询结果*********")
#     if (cls_name == "Admin"):
#         if(not os.path.exists(ADMIN_DB_PATH)):
#             print("目前还没有一个管理员")
#         usr_path = os.path.join(
#             ADMIN_DB_PATH,usr_name
#         )
#         if(os.path.exists(usr_path)):
#             with open(usr_path,mode="rb") as f:
#                 res_obj = pickle.load(f)
#             print(f"管理员{usr_name}密码为{res_obj.passwd}")
#         else:
#             print(f"管理员{usr_name}不存在")

