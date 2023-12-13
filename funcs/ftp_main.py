import threading
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import logging
from pyftpdlib.log import config_logging
config_logging(level=logging.DEBUG)

global_server = None

def runServer(path, enableAuth, username, password):
    global global_server  # 使用全局变量
    author = DummyAuthorizer()
    
    if enableAuth:
        # 如果提供了用户名和密码，则添加指定用户
        author.add_user(username, password, path, perm="elradfmw")
    else:
        # 否则，添加匿名用户
        author.add_anonymous(path, perm="elradfmw")

    handler = FTPHandler
    handler.log_level = None
    handler.authorizer = author

    # 创建FTP服务器并启动
    server = FTPServer(("", 2121), handler)

    # 使用线程在后台运行服务器
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    global_server = server

def stopServer():
    global global_server
    if global_server:
        # 关闭FTP服务器
        global_server.close_all()
    else:
        print("Server not running")