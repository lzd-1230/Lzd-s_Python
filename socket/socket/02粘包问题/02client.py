import socket
import struct
import json
"""
解决粘包问题的客户端
"""
def main():
    # 创建套接字
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 获取dest_ip dest_port
    # dest_ip = input("请输入目标ip:")
    # dest_port = int(input("请输入目标端口:"))
    dest_addr = ("121.4.162.140",9000)

    # 链接服务器
    client_socket.connect(dest_addr)
    while True:
        # 输入命令
        cmd = input("请输入命令:")
        client_socket.send(cmd.encode("utf-8"))
        print("成功发送命令")
        
        # 接收客户端header的大小
        header_size = client_socket.recv(4)
        header_size = struct.unpack("i", header_size)[0] 
        print(f"接收头部大小成功,头部大小为:{header_size}")

        # 接收头部信息
        header = client_socket.recv(header_size)
        header = json.loads(header.decode("utf-8")) # 转换成字典格式
        res_size = header["res_size"] # 拿到命令返回结果的大小
        print(f"命令结果大小为 {res_size}")

        # 开始接收命令
        cur_size = 0
        while cur_size<res_size:
            cmd_res = client_socket.recv(1024)
            cur_size += len(cmd_res) 
            print(cmd_res.decode("utf-8"), end="")

    # 关闭套接字
    client_socket.close()

if __name__ == "__main__":
    main()