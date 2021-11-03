# 多进程http服务器
import socket
import re
import multiprocessing
from httpfun.HttpService import *
from web_frame import application

class WSGIServer:
    def __init__(self):
        # 创建套接字
        self.tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcp_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        # 绑定本地ip
        self.tcp_server.bind(("",7890))
        # 设置为被动模式(listen)
        self.tcp_server.listen(5)

        self.service = HTTP() # 将服务对象实例化

    def run(self):
        while True:
            # 等待连接(accept),这里会堵塞直到有第一个客户端连接
            print("----waiting for connect----")
            client_socket,client_addr = self.tcp_server.accept()
            print("----finish connect----")
            p = multiprocessing.Process(target=self.service.server_service,
                                        args=(client_socket,client_addr,))
            # 发送数据给客户端
            p.start()
            # 主进程关闭套接字
            client_socket.close() # 多进程会使得fd的引用数++

        self.tcp_server.close()

if __name__ == "__main__":
    wsgi_server = WSGIServer() # 创建套接字
    wsgi_server.run()