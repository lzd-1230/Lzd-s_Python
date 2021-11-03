with open("./file_model/study/passwd.txt",mode="r") as f:
    for line in f:
        usrname,passwd = line.strip().split(":")
        if(usrname == "lzd" and passwd == "1122"):
            print("成功登录")
            break
    # 如果else没有被break才会进入else
    else:
        print("账号或密码错误")