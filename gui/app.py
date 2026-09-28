import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("ROS2 turtle Control")
        
        reset_btn = QPushButton(text = "turtle RESET")
        db_btn = QPushButton(text = "DB write")
        left = QPushButton(text = "←")
        up = QPushButton(text = "↑")
        down = QPushButton(text = "↓")
        right = QPushButton(text = "→")

        reset_btn.clicked.connect(self.resetturtle)
        db_btn.clicked.connect(self.dbwrite)
        left.clicked.connect(self.goleft)
        up.clicked.connect(self.goup)
        down.clicked.connect(self.godown)
        right.clicked.connect(self.goright)

        arrow = QGridLayout()
        arrow.addWidget(up, 0, 1)
        arrow.addWidget(left, 1, 0)
        arrow.addWidget(down, 1, 1)
        arrow.addWidget(right, 1, 2)

        func = QVBoxLayout()
        func.addWidget(reset_btn)
        func.addWidget(db_btn)
        func.addStretch(1)

        allgui = QHBoxLayout()
        allgui.addLayout(arrow)
        allgui.addLayout(func)


        widget = QWidget()
        widget.setLayout(allgui)
        self.setCentralWidget(widget)

    def resetturtle(self):
        print("reset")

    def dbwrite(self):
        print("db")

    def goup(self):
        print("up")

    def godown(self):
        print("down")

    def goright(self):
        print("right")

    def goleft(self):
        print("left")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()
