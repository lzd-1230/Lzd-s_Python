import os,shutil
import rarfile

# print(os.listdir())
if not os.path.isdir("./data"):
    os.mkdir("./data")

for file_name in os.listdir():
    if(file_name.endswith("rar")):
        real_name = file_name.split(".")[0]
        # print(real_name)
        rar_file = rarfile.RarFile(file_name,mode="r")
        # rar_file.extractall("./data/")
        names = rar_file.namelist()
        for f in names:
            if f.endswith("mp4"):
                rar_file.extract(f,"./data/")
        # 将加压出来多余的路径裁剪掉
        dir_name = "./data/"+real_name+"/"
        for f in os.listdir(dir_name):
            # print(f) 
            shutil.move(dir_name+f,"./data")
        os.rmdir(dir_name)

    
