import socket
import re
import os
from web_frame import application

class HTTP:
    def __init__(self):
        self.status = ""
        self.headers = ""

    def tackle_request(self,request_info):
        """解析用户的请求"""
        request_lines = request_info.splitlines()
        # print(">>"*10)
        # print(request_lines)
        # print(">>"*10)
        
        # 区分动态和静态请求
        if request_lines:
            # 找到请求的文件名
            ret = re.match(r"[^/]+([^ ]*)",request_lines[0])  # 取出请求的内容
            if ret:
                file_name = ret.group(1)
                # 默认访问index页面
                if file_name == "/":
                    file_name = "/index.html"
        return file_name

    def server_service(self,client_socket,request_info):
        """返回资源"""
        # 请求头 GET /index.html HTTP/1.1......
        request_info = client_socket.recv(1024).decode("utf-8")
        print(">>>"*10)
        print(request_info)
        print(">>>"*10)
        # 请求内容
        file_name = self.tackle_request(request_info)# .decode("utf-8")
        # print(file_name)

        # 对资源进行区分
        # 静态资源
        if not file_name.endswith(".ppp"):  
            try:  # 打开一个文件是一件很危险的事情
                f = open("./html"+file_name,"rb")
            except:
                respond_info = "HTTP/1.1 404 NOT FOUND \r\n"
                respond_info += "\r\n"
                respond_info += "----------file not found------------"
                # 发送数据
                client_socket.send(respond_info.encode("utf-8"))
            # 准备发送数据
            else:
                html_content = f.read()
                f.close()
                respond_info = "HTTP/1.1 200 OK\r\n"  # 返回一个标准的应答
                respond_info += "\r\n"
                # 将内容发送给浏览器
                client_socket.send(respond_info.encode("utf-8"))
                client_socket.send(html_content)

        # 动态资源请求
        else:
            env_dict = {"file_name":file_name}
            # 接受框架的返回值
            body = application(env_dict,self.handle_request)
            # 将框架的信息和服务器要返回的信息整合
            headers = f"HTTP/1.1 {self.headers[0]}\r\n"
            for tmp in self.headers:
                headers += f"{tmp[0]}:{tmp[1]}\r\n"
            headers += "\r\n"

            client_socket.send((headers+body).encode("utf8"))

        client_socket.close()
    

    def handle_request(self,status, headers):
        self.status = status
        self.headers = headers