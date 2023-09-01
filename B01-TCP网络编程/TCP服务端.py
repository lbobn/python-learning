import socket

if __name__ == '__main__':
    tcp_server_socket = socket.socket()

    tcp_server_socket.bind(("127.0.0.1", 8080))
    tcp_server_socket.listen(1)
    conn, address = tcp_server_socket.accept()

    result = conn.recv(1024).decode()
    print(f"{address}发送来了{result}")
    conn.send("收到".encode(encoding="utf-8"))
    conn.close()
    tcp_server_socket.close()
