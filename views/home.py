from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QFrame, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy, QLabel
from qfluentwidgets import (FluentWindow, SubtitleLabel, setFont, TogglePushButton, LineEdit, PushButton, SpinBox)
from qfluentwidgets import FluentIcon as FIF

class homeInterface(QFrame):
    def __init__(self, title:str, parent=None):
        super().__init__(parent=parent)
        self.vBoxLayout = QVBoxLayout(self)
        horizontal_layout = QHBoxLayout()
        horizontal_layout.setContentsMargins(20, 20, 20, 20)

        # 左侧布局
        leftSide=QVBoxLayout()

        # 路径选择
        pathSelecter=QHBoxLayout()
        # 路径输入框
        pathInput=LineEdit()
        pathInput.setEnabled(False)
        pathInput.setText("hello")
        # 路径浏览按钮
        pathSelectButton=PushButton("浏览")
        # 添加到路径选择
        pathSelecter.addWidget(pathInput)
        pathSelecter.addWidget(pathSelectButton)

        # 端口选择
        portSelector=QHBoxLayout()
        # 端口选择文本
        portLabel=QLabel("FTP服务端口:")
        portLabel.setStyleSheet("font-size: 15px")
        # 端口选择框
        portInput=SpinBox()
        portInput.setValue(21)
        portInput.setFixedWidth(140)
        # 添加到端口选择
        portSelector.addWidget(portLabel)
        portSelector.addWidget(portInput)
        portSelector.setAlignment(Qt.AlignmentFlag.AlignLeft)

        leftSide.addLayout(pathSelecter)
        leftSide.addLayout(portSelector)

        rightSide=QVBoxLayout()

        horizontal_layout.addLayout(leftSide)
        horizontal_layout.addLayout(rightSide)

        spacer_item = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        horizontal_layout.addSpacerItem(spacer_item)

        # 运行按钮
        runbuttonLayout=QHBoxLayout()
        runButton = TogglePushButton("启动服务")
        runButton.setFixedWidth(100)
        runbuttonLayout.addWidget(runButton)
        runbuttonLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.vBoxLayout.addLayout(horizontal_layout)
        self.vBoxLayout.addLayout(runbuttonLayout)
        self.setObjectName("homeView")