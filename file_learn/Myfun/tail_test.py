import time

cnt = 0

# 在文件末尾追加内容,用以测试tail文件的正确性
while(True):
    cnt += 1
    with open("./file_model/Myfun/test.txt",mode="at",encoding="utf-8") as f:
        f.write(f"{cnt} {cnt} {cnt}\n")
        time.sleep(1)
        print("已成功写入")
