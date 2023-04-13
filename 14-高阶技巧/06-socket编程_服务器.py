"""
服务器
"""

import socket

socket_server = socket.socket()

socket_server.bind(("localhost", 8888))

socket_server.listen(1)

conn, address = socket_server.accept()

print(f"接收到客户端连接:客户端信息为:{address}")
while True:
    data: str = conn.recv(1024).decode("UTF-8")

    print(f"客户端发来信息:{data}")
    msg = input("请输入要发送的消息:")
    if msg == "exit":
        break
    conn.send(msg.encode("UTF-8"))

conn.close()
socket_server.close()
