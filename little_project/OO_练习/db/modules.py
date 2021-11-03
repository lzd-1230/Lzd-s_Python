"""
该文件用于存放类
"""
from db import db_header

class Admin(object):
    def __init__(self,usr_name,passwd):
        self.usr_name = usr_name
        self.passwd = passwd
    
    # 保存对象
    def save(self):
        db_header.save_data(self)
    
    @classmethod
    def select(cls):
        pass
    