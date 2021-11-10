import re

""" 同时使用多个分隔符来分割 """
line = "asdf fjdk; afed, fjek,asdf,    foo    asd"
r = re.compile(r'[;,\s]\s*')
print(r.search(line)) # 利用正则表达式去匹配分隔符,从而实现多种分隔符