"""
入口文件
"""
import os
import sys
from core import src
# 添加解释器路径
sys.path.append(
    os.path.dirname(__file__) # 将当前目录添加到解释器
)

# 开始执行项目函数
if __name__ == "__main__":
    # 先执行用户视图层
    src.run()

    