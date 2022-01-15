import socket
from gevent import spawn
from gevent import monkey;monkey.patch_all()

def communicate(conn):
    while True:
        try:
            data = conn.recv(1024) # 这里有IO操作
            if len(data) == 0: break
            conn.send(data.upper())
        except Exception as e:
            print(e)
            break
    conn.close()

def server(ip,port):
    server = socket.socket()
    server.bind((ip,port))
    server.listen(5)

    while True:
        conn, addr = server.accept() # 这里是IO
        spawn(communicate,conn) # 监听communicate里面的IO操作

if __name__ == "__main__":
    g1 = spawn(server,"127.0.0.1",8100) # 监听server中的IO操作
    g1.join()