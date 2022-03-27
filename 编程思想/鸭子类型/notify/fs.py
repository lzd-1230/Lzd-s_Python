class Fs():
    def __init__(self,content) -> None:
        self.content = content
        
    def send(self):
        print(f"飞书发送{self.content}")