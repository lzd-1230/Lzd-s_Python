with open("./file_model/study/passwd.txt",mode="at",encoding="utf-8") as f:
    name = input("输入账号:")
    passwd = input("输入密码")
    f.write(f"{name}:{passwd}\n")
