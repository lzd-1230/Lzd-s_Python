import datetime
import time
# 可以进行任意时间维度的平移:比如查看三天前创建的所有时间!
# print(datetime.datetime.now() + datetime.timedelta(days=-3))

# 结构化时间(时间戳和字符串相互转换的中间变量)
struct_time = time.localtime()
time_stamp = time.mktime(struct_time)
print(time_stamp) # 将结构化的时间->时间戳
time_str = time.strftime("%X",struct_time)
print(time_str)


# 将字符串转换成时间变量
time_str = "2001-11-22 19:21:22"
struct_time = time.strptime(time_str,"%Y-%m-%d %H:%M:%S")
print(struct_time)

"""如果用户续费了会员,应该如何cao操作"""
# 1.从文件中读出到期时间
deadline = time_str

deadline_struct = time.strptime(deadline,"%Y-%m-%d %H:%M:%S")
deadline_stamp = time.mktime(deadline_struct)
# print(time.mktime(deadline_struct)) # 截止日期的时间戳
deadline_stamp_update = deadline_stamp+7*86400 # 续费七天

deadline_pro = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(deadline_stamp_update))
print("更新后的截止时间",deadline_pro)


