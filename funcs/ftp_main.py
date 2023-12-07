from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import logging
from pyftpdlib.log import config_logging
config_logging(level=logging.ERROR)


def runServer():
    author = DummyAuthorizer()
    author.add_anonymous("/Volumes/T7_Shield", perm="elradfmw")

    handler = FTPHandler
    handler.log_level = None
    handler.authorizer = author

    # 创建FTP服务器并启动
    server = FTPServer(("", 2121), handler)
    server.serve_forever()