# echo-client.py

import socket


class Client:
    HOST = "localhost"  # The server's hostname or IP address
    PORT = 8080  # The port used by the server

    def __init__(self):
        pass

    def start_client(self):
        print("running client")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            s.sendall(b"Hello, world")
            data = s.recv(1024)

        print(f"Received {data!r}")
