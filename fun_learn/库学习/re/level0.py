import re

# 题1
text = "My Name is Adam and I come from Beijing "
target = "MAB"

res = re.search("(M[a-z]+) .*? (A[a-z]+) .*? (B[a-z]+)",text)
print(res.group(1) + res.group(2) + res.group(3))


# 题2
text = "abc,23,456 ,789, mnp"
role = re.compile(r"(\s?,\s?)")
res = role.sub("",text)
# print(res)

# 题3


