import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/d-vinn/ros2_study/src/ros-turtle-control/ros-turtle-control/install/my-test-package'
