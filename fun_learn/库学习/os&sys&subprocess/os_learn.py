import os
"""
常用API:
    os文件操作
        os.makedirs(PATH) # 递归创建文件夹
        os.mkdir() # 创建文件夹
        os.chdir() # 改变当前文件路径
        os.remove() # 删除文件
        os.rmdir(<src>,<dst>) # 删除目录

    os.path系列
        os.path.listdir(PATH) # 某些目录下的文件名
        os.path.join(path1,path2,path3,...) # 将路径拼接起来
        os.path.dirname(<file_path>) # 获取文件的目录名
        os.path.normpath(<PATH>) # 规范化路径,针对不同平台
"""


dirname = r"F:\\file_sum2.0\\Python\\MyPython\\多任务"
def cal_dir_size(path):
    """
    统计文件夹大小的功能
    """
    dir_size = 0
    for son_path in os.listdir(path):
        son_path = os.path.join(path,son_path)
        if os.path.isfile(son_path):
            dir_size += os.path.getsize(son_path)
            # print(son_path,os.path.getsize(son_path))

        elif(os.path.isdir(son_path)):
            cal_dir_size(son_path)
    return dir_size
print(cal_dir_size(dirname)) # 为啥最后所有的文件大小都是4096啊???
