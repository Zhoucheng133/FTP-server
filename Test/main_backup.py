from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget, QHBoxLayout, QSizePolicy
from PyQt6.QtGui import QPixmap, QMouseEvent
from PyQt6.QtCore import Qt, QPoint, QPointF

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
    
    def mousePressEvent(self, event: QMouseEvent):
        self.drag_start_position = event.globalPosition()

    def mouseMoveEvent(self, event: QMouseEvent):
        delta = event.globalPosition() - self.drag_start_position
        delta_pointf = QPointF(delta)
        self.move(self.pos() + delta_pointf.toPoint())
        self.drag_start_position = event.globalPosition()

    def titleBar(self):
        titleBarContent = QHBoxLayout()
        titleBarContent.setSpacing(0)
        titleBarContent.setAlignment(Qt.AlignmentFlag.AlignRight)

        # 可拖动区域
        dragArea=QLabel(self)
        dragArea.setFixedSize(340,30)
        self.drag_start_position = QPoint(0, 0)
        # 信号连接到事件处理函数
        dragArea.mousePressEvent = self.mousePressEvent
        dragArea.mouseMoveEvent = self.mouseMoveEvent
        # dragArea.mouseReleaseEvent = self.mouseReleaseEvent

        # 最小化按钮
        minButton=QLabel(self)
        pixmap = QPixmap("assets/minus.svg")
        minButton.setPixmap(pixmap)
        minButton.setFixedSize(30,30)
        minButton.setAlignment(Qt.AlignmentFlag.AlignCenter)
        minButton.setStyleSheet("font-size: 16pt;")
        minButton.setCursor(Qt.CursorShape.PointingHandCursor)
        minButton.mousePressEvent = self.minApp

        # 关闭按钮
        closeButton=QLabel(self)
        pixmap = QPixmap("assets/close.svg")
        closeButton.setPixmap(pixmap)
        closeButton.setFixedSize(30,30)
        closeButton.setStyleSheet("""
            background-color: red; 
            font-size: 12pt;
            color: white;
            border-bottom-left-radius: 5px;
        """)
        closeButton.setAlignment(Qt.AlignmentFlag.AlignCenter)
        closeButton.setCursor(Qt.CursorShape.PointingHandCursor)
        closeButton.mousePressEvent = self.quitApp
        
        titleBarContent.addWidget(dragArea)
        titleBarContent.addWidget(minButton)
        titleBarContent.addWidget(closeButton)
        return titleBarContent
    
    def minApp(self, event):
        # 最小化窗口
        self.showMinimized()

    def quitApp(self, event):
        # 处理关闭事件
        QApplication.instance().quit()


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
