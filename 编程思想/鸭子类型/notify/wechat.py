class Wechat():
    def __init__(self,content) -> None:
        self.content = content
        
    def send(self):
        print(f"微信发送{self.content}")