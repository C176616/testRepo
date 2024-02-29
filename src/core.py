import helloworld.helloworld as sh
from client import Client
import os

def make_client():
    m_client = Client()
    m_client.start_client()
    m_client.send_message("this is going to server")

# def check_env_variables():
#     env_variable_value = os.environm(["INITIAL_VALUE"])
#     return float(env_variable_value)

def say_hello():
    # this has to be a comment d
    return sh.hello_world()
