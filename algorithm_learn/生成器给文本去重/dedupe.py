import os 
import re
def dedupe(f):
    seen = set()
    for line in f:
        val = re.sub("\n","",line) # 注意为了区分最后一行没有换行
        if(val not in seen):
            yield line
            seen.add(val)

os.chdir(os.path.dirname(__file__))        

with open("./test.txt",mode="r",encoding="utf-8") as f_in:
    with open("./out.txt",mode="w",encoding="utf-8") as f_out:
        # 1.整个读进去然后扔出来
        content = list(dedupe(f_in))
        print(content)
        for c in content:
            f_out.write(c)
    