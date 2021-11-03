from collections import deque

"""
队列库的基本使用
"""
# q = deque(maxlen=3)
# q.append("3")
# print(q.pop())

"""
保留最后N个元素
"""
# def search(lines,pattern,history=5):
#     """
#     lines:文本内容
#     pattern:需要匹配的字段,可以换成正则
#     history:要保留的数量
#     """
#     previous_line = deque(maxlen=history)
#     for line in lines:
#         if pattern in line:
#             yield line,previous_line # 如果匹配到,就把这一行的内容和队列传回去
#         previous_line.append(line)


# if __name__ == "__main__":
#     with open("test.txt",mode="r") as f: # 这个f就是文本的每一行,对他迭代可以迭代出每一行的内容
#         for line ,previous_line in search(f,"python",2): # 直接调用生成器
#             for pline in previous_line:
#                 print("最后n项",pline)
#             print("当前行",line,end="")
#             print("-"*20)
