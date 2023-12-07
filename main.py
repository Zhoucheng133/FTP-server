from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 窗口内容
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        self.setup_layout()

        # 窗口属性
        self.setFixedSize(400, 500)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet("background-color: white;")

    def titleBar(self):
        titleBarContent = QHBoxLayout()
        titleBarContent.setSpacing(0)
        titleBarContent.setAlignment(Qt.AlignmentFlag.AlignRight)
        # 最小化按钮
        minButton=QLabel(self)
        pixmap = QPixmap("assets/minus.svg")
        minButton.setPixmap(pixmap)
        minButton.setFixedSize(30,30)
        minButton.setAlignment(Qt.AlignmentFlag.AlignCenter)
        minButton.setStyleSheet("font-size: 16pt;")

        # 关闭按钮
        closeButton=QLabel(self)
        pixmap = QPixmap("assets/close.svg")
        closeButton.setPixmap(pixmap)
        closeButton.setFixedSize(30,30)
        closeButton.setStyleSheet("background-color: red; font-size: 12pt; color: white")

        closeButton.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        titleBarContent.addWidget(minButton)
        titleBarContent.addWidget(closeButton)
        return titleBarContent


    def setup_layout(self):
        vertical_layout = QVBoxLayout(self.centralWidget())
        vertical_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        # 将两个水平布局添加到垂直布局中
        vertical_layout.addLayout(self.titleBar())

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
