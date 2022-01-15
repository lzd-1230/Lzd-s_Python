import socket
"""
远程发送命令的客户端
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
        cmd_res = client_socket.recv(1024) # 如果命令的返回结果小于1024,则可以接收,但如果返回信息过多,则可能收不干净
        print(cmd_res.decode("utf-8"))
    # 关闭套接字
    client_socket.close()

if __name__ == "__main__":
    main()