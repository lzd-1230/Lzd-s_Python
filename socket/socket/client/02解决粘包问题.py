import socket 

total_size = 123213123
recv_size = 0

# 创建套接字
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
dest_addr = ("121.4.162.140",9000)
client_socket.connect(dest_addr)
