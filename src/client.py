# echo-client.py

import socket


class Client:
    HOST = "localhost"  # The server's hostname or IP address
    PORT = 8080  # The port used by the server

    def __init__(self):
        print("created client")

    def start_client(self):
        return "running client"

    def send_message(self, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            # s.sendall(b"this is from the server")
            s.sendall(message.encode("utf-8"))
            data = s.recv(1024)
            result = data.decode()

        # return f"Received {data!r}"
        return result
