from stack import Stack

class Min_Stack(Stack):
    def __init__(self, length: int) -> None:
        super().__init__(length)
        self.min_stack = Stack(length)

    def push(self,data):
        # 栈内无元素时
        if(self.top <= 0):
            self.min_stack.push(data) 
        # 栈内有元素时
        else:
            if(data < self.min_stack.get_top()):
                self.min_stack.push(data) 
            else:
                self.min_stack.push(self.min_stack.get_top())
        super().push(data)

    def pop(self):
        if(not super().is_empty()):
            super().pop()
            self.min_stack.pop()
        else:
            print("栈空,无法出栈")
        
    def get_min(self):
        print(f"最小元素为{self.min_stack.get_top()}")
        return self.min_stack.get_top()

if __name__ == "__main__":
    min_s = Min_Stack(4)
    min_s.push(2)
    min_s.push(3)
    min_s.push(1)
    min_s.push(2)
    min_s.get_min()