import sys
import threading
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from db_update import DB, DB_CONFIG
from locate import ChangeTurtleLocate

class GuiRosPublisher(Node):
    def __init__(self):
        super().__init__('gui_ros_publisher')
        self.publisher_ = self.create_publisher(String, '/gui_command', 10)

    def send_command(self, cmd):
        msg = String()
        msg.data = cmd
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published command to C++ node: {cmd}')

class MyWindow(QMainWindow):
    def __init__(self, ros_node):
        super().__init__()
        self.ros_node = ros_node
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

        reset_btn.clicked.connect(lambda: self.action_triggered("reset", self.loc.reset))
        db_btn.clicked.connect(lambda: self.db.insert_data('turtle1', self.loc.x, self.loc.y, self.loc.theta))
        left.clicked.connect(lambda: self.action_triggered("left", self.loc.goleft))
        up.clicked.connect(lambda: self.action_triggered("up", self.loc.goup))
        down.clicked.connect(lambda: self.action_triggered("down", self.loc.godown))
        right.clicked.connect(lambda: self.action_triggered("right", self.loc.goright))

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

    def action_triggered(self, cmd_name, loc_func):
        loc_func()
        self.ros_node.send_command(cmd_name)


if __name__ == '__main__':
    rclpy.init(args=None)
    ros_node = GuiRosPublisher()

    ros_thread = threading.Thread(target=rclpy.spin, args=(ros_node,), daemon=True)
    ros_thread.start()

    app = QApplication(sys.argv)
    win = MyWindow(ros_node)
    win.show()
    sys.exit(app.exec_())
