import os
import re
train_dicts = dict()
train_dict_keys = []

for file in os.listdir("./testfile"):
    if(re.match(r"data_batch_.*[0-9]$",file)):
        train_dict_keys.append(file)
        tmp_path = os.path.join(os.getcwd(),"testfile",file)
        # print(tmp_path)
        with open(tmp_path,mode="rb") as f:
            res = f.read()
            train_dicts[file] = res
            
print(train_dict_keys)
print(train_dicts[train_dict_keys[0]])

        
 