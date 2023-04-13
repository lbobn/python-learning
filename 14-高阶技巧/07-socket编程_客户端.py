"""
客户端
"""

import socket

socket_client = socket.socket()
socket_client.connect(("localhost", 8888))
while True:
    msg = input("请输入要发送的消息:")
    if msg == "exit":
        break
    socket_client.send(msg.encode("UTF-8"))

    message = socket_client.recv(1024).decode("UTF-8")
    print(f"服务端发来消息:{message}")

socket_client.close()
