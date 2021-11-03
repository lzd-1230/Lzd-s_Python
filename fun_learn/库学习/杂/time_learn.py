import time

# 1.时间戳:从1970到现在的秒数  作用:一般用在计算时间间隔!!
print(time.time())
# 2.按照某种格式显示成字符串 一般用于展示,或者和pd.to_datetime()来进行转换
print(time.strftime("%Y-%m-%d-%H-%M-%S  %p"))
print(time.strftime("%X")) # 显示时分秒

# 3.结构化时间 作用:方便获取当前时间的某一个部分,比如分钟,年,月等
res = time.localtime()
print() 

# 
