import threading 
import socket 
import struct
import json
import subprocess
"""
通过 struct 发送 header 来解决粘包问题
"""

def client_handle(client_socket,client_addr):
    while True:
        try:
            # 接收命令文字
            cmd = client_socket.recv(1024) # 接受到的数据
            # 在服务端运行命令
            obj = subprocess.Popen(
                cmd.decode("utf-8"),
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            # 拿到命令运行的结果
            stdout_res = obj.stdout.read()
            stderr_res = obj.stderr.read()

            header = {
                "res_size":len(stdout_res+stderr_res)
            }

            header_json_str = json.dumps(header)
            header_json_bytes = header_json_str.encode("utf-8")
            header_size = len(header_json_bytes)

            # 发送headers的大小
            header_size_bytes = struct.pack("i",header_size)
            client_socket.send(header_size_bytes)

            # 发送header的内容
            client_socket.send(header_json_bytes)

            # 将结果返回给客户端
            client_socket.send((stdout_res+stderr_res),)

        except Exception as e:
            print(e)


def main():
    # 1.创建TCP监听套接字
    tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2.绑定本地IP
    tcp_server.bind(("0.0.0.0",9000))

    # 3.设置为listen模式
    tcp_server.listen(128) # 接待室大小

    while True:
        # 4.等待连接,来一个连接创建一个进程去处理
        print("----waiting for connect----")
        client_socket,client_addr = tcp_server.accept() # 建成一个链接(主进程)
        print("接收到的客户端套接字为",client_addr)
        print("----finish one connect----")

        # 想法:来一个我就创建一个线程去处理
        threading.Thread(target=client_handle,args=(client_socket,client_addr)).start()
    
if __name__ == "__main__":
    main()
