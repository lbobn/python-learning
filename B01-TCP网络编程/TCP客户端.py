import socket

if __name__ == '__main__':
    tcp_client_socket = socket.socket()

    tcp_client_socket.connect(("127.0.0.1", 8080))
    # msg = "hello world"
    tcp_client_socket.send("你好呀，hello".encode(encoding="utf-8"))
    print(tcp_client_socket.recv(1024).decode())

    tcp_client_socket.close()
