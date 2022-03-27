"""
本脚本用于按照文件修改时间给文件重命名
"""
import os
import re

file_names = os.listdir("./")
file_dict = dict()

for file_name in file_names:
    cur_time = os.stat(file_name).st_ctime
    # print(cur_time)
    file_dict[file_name] = cur_time

file_sorted = sorted(file_dict,key=lambda k:file_dict[k])

# 给某一特定格式的文件重命名
for idx,file_name in enumerate(file_sorted):
    if(re.match(".*\.flv$",file_name)):
        os.rename(file_name,f"{idx}.flv")