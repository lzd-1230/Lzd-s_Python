class Qq():
    def __init__(self,content) -> None:
        self.content = content
        
    def send(self):
        print(f"QQ发送{self.content}")