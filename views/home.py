from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QFrame, QHBoxLayout, QVBoxLayout
from qfluentwidgets import (FluentWindow, SubtitleLabel, setFont, TogglePushButton)
from qfluentwidgets import FluentIcon as FIF

class homeInterface(QFrame):
    def __init__(self, title:str, parent=None):
        super().__init__(parent=parent)
        self.vBoxLayout = QVBoxLayout(self)
        horizontal_layout = QHBoxLayout()
        runButton = TogglePushButton("启动服务")

        self.vBoxLayout.addLayout(horizontal_layout)
        self.vBoxLayout.addWidget(runButton)
        self.setObjectName("homeView")