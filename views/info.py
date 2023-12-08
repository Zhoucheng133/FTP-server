from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QFrame, QHBoxLayout, QVBoxLayout
from qfluentwidgets import (FluentWindow, SubtitleLabel, setFont, TogglePushButton)
from qfluentwidgets import FluentIcon as FIF

class infoInterface(QFrame):
    def __init__(self, text: str, parent=None):
        super().__init__(
            parent=parent
        )
        self.vBoxLayout = QVBoxLayout(self)

        self.setObjectName("infoView")