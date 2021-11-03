"""
配置文件
    用于一些路径的配置
"""
import os

BASE_PATH = os.path.dirname(
    os.path.dirname(__file__)
)

DB_PATH = os.path.join(
    BASE_PATH,"db"
)