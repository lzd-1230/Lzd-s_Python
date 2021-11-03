import pickle

res = pickle.dumps({1,2,3,4,5})
print(res)
# 将序列化后的内容写入
with open("./test.pkl",mode="wb") as f:
    f.write(res)

# 从本地读入序列化后的内容
with open("./test.pkl",mode="rb") as f:
    read_res = f.read()
print(pickle.loads(read_res))