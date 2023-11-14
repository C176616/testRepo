import pytest
from client import Client


# class Client:
#     HOST = "localhost"  # The server's hostname or IP address
#     PORT = 8080  # The port used by the server

#     def __init__(self):
#         print("created client")

#     def start_client(self):
#         print("running client")

#     def send_message(self, message):
#         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#             s.connect((self.HOST, self.PORT))
#             # s.sendall(b"this is from the server")
#             s.sendall(message.encode("utf-8"))
#             data = s.recv(1024)

#         print(f"Received {data!r}")


@pytest.fixture()
def setup():
    return Client()


def test_start_client(setup):
    result = setup.start_client()
    assert result == "running client"


def test_send_message(setup):
    setup.start_client()
    result = setup.send_message("this is my message")
    assert result == "this is my message"
