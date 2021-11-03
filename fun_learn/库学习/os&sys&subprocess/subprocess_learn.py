import subprocess
"""
更深入的用法在进程部分再补充
"""

# 基本用法:执行shell命令
obj = subprocess.Popen("echo 123",shell=True,stdout=subprocess.PIPE,\
                                stderr=subprocess.PIPE
                        )
res_true = obj.stdout.read()
res_err = obj.stderr.read()

print(res_true.decode("gbk"))
# print(res_err.decode("gbk"))