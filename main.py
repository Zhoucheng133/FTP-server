# coding:utf-8
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QFrame, QHBoxLayout, QWidget, QSizePolicy
from qfluentwidgets import (FluentWindow, SubtitleLabel, setFont)
from qfluentwidgets import FluentIcon as FIF

from views.home import homeInterface
from views.info import infoInterface

class Window(FluentWindow):

    def __init__(self):
        super().__init__()

        # create sub interface
        self.homeInterface = homeInterface(self)
        self.infoInterface = infoInterface(self)

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, '主页')
        self.addSubInterface(self.infoInterface, FIF.INFO, '关于')

    def initWindow(self):
        self.setFixedSize(900, 700)
        # NOTE 添加图标
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
        self.setWindowTitle('FTP Server')

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
