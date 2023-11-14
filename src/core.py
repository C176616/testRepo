import helloworld.helloworld as sh
from client import Client


def make_client():
    m_client = Client()
    m_client.start_client()
    return sh.hello_world()
