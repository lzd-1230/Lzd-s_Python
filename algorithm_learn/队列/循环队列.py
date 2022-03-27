"""
用循环数组实现队列
    实现循环的关键就是以一个长度+1的数组来取余滚动实现
"""
import numpy

class Queque():
    def __init__(self,length,data:list = None):
        self.len = length
        self.que = data
        # 初始化一下
        self.init()
    
    def init(self):
        if(not self.que):
            self.que = list(numpy.zeros(self.len+1))
        self.front = self.rear = 0

    def is_full(self):
        if((self.rear+1)%(self.len+1) == self.front):
            return True
        
    def enter_que(self,data):
        if(self.is_full()):
            print("队列已满")
            return False
        else:
            self.que[self.rear] = data
            self.rear = (self.rear+1)%(self.len+1)
    
    def travel_que(self):
        point = self.front
        while(point%(self.len+1) < self.rear):
            print(self.que[point])
            point = (point+1)%(self.len+1)

if __name__ == "__main__":
    q = Queque(3)
    q.enter_que("a")
    q.travel_que()
    q.enter_que("b")
    q.travel_que()
    q.enter_que("c")
    q.travel_que()