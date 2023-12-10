from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QFrame, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy, QLabel, QFileDialog
from qfluentwidgets import (FluentWindow, SubtitleLabel, setFont, TogglePushButton, LineEdit, PushButton, SpinBox, SwitchButton, PasswordLineEdit, CheckBox, Flyout, FluentIcon, InfoBarIcon)

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
        self.pathSelectButton=PushButton("浏览")
        self.pathSelectButton.clicked.connect(self.selectPath)
        # 添加到路径选择
        pathSelecter.addWidget(self.pathInput)
        pathSelecter.addWidget(self.pathSelectButton)

        # 端口选择
        portSelector=QHBoxLayout()
        # 端口选择文本
        portLabel=QLabel("FTP服务端口:")
        # 端口选择框
        self.portInput=SpinBox()
        self.portInput.setRange(1,10000)
        self.portInput.setValue(21)
        self.portInput.setFixedWidth(140)
        # 添加到端口选择
        portSelector.addWidget(portLabel)
        portSelector.addWidget(self.portInput)
        portSelector.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # 身份验证开关
        authSwitch=QHBoxLayout()
        # 切换开关
        self.switch=CheckBox(self)
        self.switch.stateChanged.connect(self.authChanged)
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
        self.runButton = TogglePushButton("启动服务")
        self.runButton.setFixedWidth(100)
        self.runButton.clicked.connect(self.runServer)
        runbuttonLayout.addWidget(self.runButton)
        runbuttonLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.vBoxLayout.addLayout(horizontal_layout)
        self.vBoxLayout.addLayout(runbuttonLayout)
        self.vBoxLayout.addStretch(1)
        self.setObjectName("homeView")

    def authChanged(self, state):
        self.passwordInput.setEnabled(state==2)
        self.usernameInput.setEnabled(state==2)
    
    def selectPath(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.pathInput.setText(directory)

    def errDialog(self, text):
        widgetTarget=self.runServer
        if(text=="没有选择目录"):
            widgetTarget=self.pathInput
        elif(text=="没有输入用户名"):
            widgetTarget=self.usernameInput
        elif(text=="没有输入密码"):
            widgetTarget=self.passwordInput
        Flyout.create(
            icon=InfoBarIcon.ERROR,
            title='无法继续',
            content=text,
            target=widgetTarget,
            parent=self,
            isClosable=True
        )

    def runServer(self):
        if(self.runButton.isChecked()):
            if(self.pathInput.text()==""):
                self.errDialog("没有选择目录")
                self.runButton.setChecked(False)
                return
            elif(self.switch.isChecked()==True and self.usernameInput.text()==""):
                self.errDialog("没有输入用户名")
                self.runButton.setChecked(False)
                return
            elif(self.switch.isChecked()==True and self.passwordInput.text()==""):
                self.errDialog("没有输入密码")
                self.runButton.setChecked(False)
                return
            self.pathSelectButton.setEnabled(False)
            self.portInput.setEnabled(False)
            self.switch.setEnabled(False)
            self.passwordInput.setEnabled(False)
            self.usernameInput.setEnabled(False)
        else:
            self.pathSelectButton.setEnabled(True)
            self.portInput.setEnabled(True)
            self.switch.setEnabled(True)
            if(self.switch.isChecked()):
                self.passwordInput.setEnabled(True)
                self.usernameInput.setEnabled(True)
