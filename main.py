from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import logging
from pyftpdlib.log import config_logging
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt

config_logging(level=logging.ERROR)

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 500)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet("background-color: white;")

if __name__ == "__main__":
    app = QApplication([])
    main_window = MyMainWindow()
    main_window.show()
    app.exec()
