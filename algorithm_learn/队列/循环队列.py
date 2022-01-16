"""
用循环数组实现队列
"""
class Queque():
    def __init__(self,num,data:list = None):
        self.len = num
        self.data = []
        # 初始化一下
        for i in range(num):
            if(data):
                self.data.append(data[i])
            else:
                self.data.append(0)
        self.front = self.rear = 0

    def is_full(self):
        
    def enter_que(self):
        pass
