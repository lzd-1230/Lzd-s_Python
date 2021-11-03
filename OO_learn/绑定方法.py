import setting

class MySQL():
    def __init__(self,ip,port):
        self.ip = ip 
        self.port = port

    @classmethod
    def format_obj(cls):
        return cls(setting.IP,setting.PORT)


x = MySQL(None,None).format_obj()
# 
print(x.ip,x.port)
