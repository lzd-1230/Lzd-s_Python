import os

def show_dir(deep,dir_path="./"):
    deep += 1
    size = 0
    for p in os.listdir(dir_path):
        rel_path = os.path.join(dir_path,p)
        if os.path.isdir(rel_path):
            size += show_dir(deep,rel_path,)
        else:
            size += os.path.getsize(rel_path)
    if deep == 2:
        print(f"{dir_path}的目录大小为:{size//1024**2}MB")
    return size

path = input("请输入要查看的目录路径(默认为当前路径)")
mode = input("请选择输出的格式(1:KB, 2:MB, 3:GB)")
if not path:
    total_size = show_dir(deep)
else:
    total_size = show_dir(0,path)

if mode == str(1):
    print(f"总目录大小为{total_size//1024}KB")
elif mode == str(2):
    print(f"总目录大小为{total_size//1024**2}MB")
elif mode == str(3):
    print(f"总目录大小为{total_size//1024**3}GB")
elif mode == "":
    print(f"总目录大小为{total_size//1024**2}MB")