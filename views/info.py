from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QApplication, QFrame, QHBoxLayout, QVBoxLayout, QLabel
from qfluentwidgets import (FluentWindow, SubtitleLabel, setFont, TogglePushButton)
from qfluentwidgets import FluentIcon as FIF

class infoInterface(QFrame):
    def __init__(self, text: str, parent=None):
        super().__init__(
            parent=parent
        )
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        self.vBoxLayout.setSpacing(0)

        # 图标
        self.iconImg=QLabel(self)
        self.pixmap = QPixmap('assets/icons/tmpIcon.png')
        self.pixmap=self.pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio)
        self.iconImg.setPixmap(self.pixmap)
        self.iconImg.setFixedSize(self.pixmap.width(), self.pixmap.height())
        self.vBoxLayout.addWidget(self.iconImg)

        # App名称
        self.appName=QLabel("FTP Server")
        self.appName.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.appName.setStyleSheet("font-size: 18px; font-weight: bolder; margin-top: 10px")
        self.vBoxLayout.addWidget(self.appName)

        # 版本号
        self.versionName=QLabel("Development Insider")
        self.versionName.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.versionName.setStyleSheet("color: #B5B5B5; margin-top: 5px")
        self.vBoxLayout.addWidget(self.versionName)

        # 依赖
        self.baseList=QLabel("Based on pyQt, pyftpdlib & QFluent")
        self.baseList.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.baseList.setStyleSheet("color: #B5B5B5; margin-top: 15px")
        self.vBoxLayout.addWidget(self.baseList)

        # 对象名称
        self.setObjectName("infoView")