import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from db_update import DB, DB_CONFIG
from locate import ChangeTurtleLocate

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.loc = ChangeTurtleLocate()
        self.db = DB(**DB_CONFIG)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("ROS2 turtle Control")
        
        reset_btn = QPushButton(text = "turtle RESET")
        db_btn = QPushButton(text = "DB write")
        left = QPushButton(text = "←")
        up = QPushButton(text = "↑")
        down = QPushButton(text = "↓")
        right = QPushButton(text = "→")

        reset_btn.clicked.connect(self.loc.reset)
        db_btn.clicked.connect(lambda: self.db.insert_data('turtle1', self.loc.x, self.loc.y, self.loc.theta))
        left.clicked.connect(self.loc.goleft)
        up.clicked.connect(self.loc.goup)
        down.clicked.connect(self.loc.godown)
        right.clicked.connect(self.loc.goright)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
