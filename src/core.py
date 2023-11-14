import helloworld.helloworld as sh
from client import Client


def make_client():
    m_client = Client()
    m_client.start_client()
    m_client.send_message("this is going to server")


def say_hello():
    return sh.hello_world()
