"""
要求实现一个带有弹出最小值方法O(1)的栈
    多加一个最小栈
"""
class Stack():
    def __init__(self,length:int) -> None:
        self.stack = []
        self.top = 0 # 表示当前栈顶元素的下标
        self.len = length
    
    def is_full(self):
        if(self.top>=self.len):
            return True
        else:
            return False
    def is_empty(self):
        if(self.top == None):
            print("栈为空")
            return True 
        else: 
            return False 
    
    def push(self,data):
        if(self.is_full()):
            print("栈已满")
            return False
        else:
            self.stack.append(data)
            self.top += 1
            return True
    def pop(self):
        if(self.is_empty()):
            return None
        else:
            return self.stack.pop()

    def get_top(self):
        return self.stack[self.top-1]

    def travel(self):
        for idx in range(self.len):
            print(self.stack[idx])


if __name__ == "__main__":
    s = Stack(3)
    s.push("a")
    s.push("b")
    s.push("c")
    s.travel() 
    s.push("d")

