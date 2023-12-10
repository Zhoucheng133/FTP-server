from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QFrame, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy, QLabel, QFileDialog
from qfluentwidgets import (FluentWindow, SubtitleLabel, setFont, TogglePushButton, LineEdit, PushButton, SpinBox, SwitchButton, PasswordLineEdit)
from qfluentwidgets import FluentIcon as FIF

class homeInterface(QFrame):

    def __init__(self, title:str, parent=None):
        super().__init__(parent=parent)
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.addStretch(1)
        horizontal_layout = QHBoxLayout()
        horizontal_layout.setContentsMargins(20, 20, 20, 20)

        # 左侧布局
        leftSide=QVBoxLayout()

        # 路径选择
        pathSelecter=QHBoxLayout()
        # 路径输入框
        self.pathInput=LineEdit()
        self.pathInput.setEnabled(False)
        # 路径浏览按钮
        pathSelectButton=PushButton("浏览")
        pathSelectButton.clicked.connect(self.selectPath)
        # 添加到路径选择
        pathSelecter.addWidget(self.pathInput)
        pathSelecter.addWidget(pathSelectButton)

        # 端口选择
        portSelector=QHBoxLayout()
        # 端口选择文本
        portLabel=QLabel("FTP服务端口:")
        portLabel.setStyleSheet("font-size: 15px")
        # 端口选择框
        portInput=SpinBox()
        portInput.setRange(1,10000)
        portInput.setValue(21)
        portInput.setFixedWidth(140)
        # 添加到端口选择
        portSelector.addWidget(portLabel)
        portSelector.addWidget(portInput)
        portSelector.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # 身份验证开关
        authSwitch=QHBoxLayout()
        # 切换开关
        self.switch=SwitchButton(self)
        self.switch.checkedChanged.connect(self.authChanged)
        # 提示文本
        switchLabel=QLabel("开启身份验证")

        authSwitch.addWidget(switchLabel)
        authSwitch.addWidget(self.switch)

        leftSide.addLayout(pathSelecter)
        leftSide.addLayout(portSelector)
        leftSide.addLayout(authSwitch)

        # 右侧布局
        rightSide=QVBoxLayout()

        # 用户名和密码
        authArea=QVBoxLayout()
        authArea.setSpacing(0)
        # 用户名部分
        usernameLabel=QLabel("用户名")
        usernameLabel.setStyleSheet("margin-top: 10px; margin-bottom: 10px")
        self.usernameInput=LineEdit(self)
        self.usernameInput.setEnabled(False)
        # 密码部分
        passwordLabel=QLabel("密码")
        passwordLabel.setStyleSheet("margin-top: 10px; margin-bottom: 10px")
        self.passwordInput=PasswordLineEdit(self)
        self.passwordInput.setEnabled(False)

        authArea.addWidget(usernameLabel)
        authArea.addWidget(self.usernameInput)
        authArea.addWidget(passwordLabel)
        authArea.addWidget(self.passwordInput)

        rightSide.addLayout(authArea)

        leftSide.addStretch()
        rightSide.addStretch()
        horizontal_layout.setSpacing(20)
        horizontal_layout.addLayout(leftSide, 1)
        horizontal_layout.addLayout(rightSide, 1)

        # 运行按钮
        runbuttonLayout=QHBoxLayout()
        runButton = TogglePushButton("启动服务")
        runButton.setFixedWidth(100)
        runButton.clicked.connect(self.runServer)
        runbuttonLayout.addWidget(runButton)
        runbuttonLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.vBoxLayout.addLayout(horizontal_layout)
        self.vBoxLayout.addLayout(runbuttonLayout)
        self.vBoxLayout.addStretch(1)
        self.setObjectName("homeView")

    def authChanged(self):
        self.passwordInput.setEnabled(self.switch.checked)
        self.usernameInput.setEnabled(self.switch.checked)
    
    def selectPath(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.pathInput.setText(directory)

    def runServer(self):
        print("运行")