# ROS2 Turtle Control with PyQt & MySQL

PyQt5 GUI를 통해 ROS2 Turtlesim 제어 및 거북이의 위치와 동작 정보를 MySQL(WSL) 데이터베이스에 저장하는 프로젝트

---

## 요구사항 
* Ubuntu 22.04 (WSL2 환경)
* ROS2 Humble
* Python 3.10+
* MySQL Server (WSL 환경)

---

## 실행 방법 

### 1. 저장소 클론 및 이동
```bash
git clone https://github.com/d-vinn/ros-turtle-control.git
cd ros-turtle-control
```
### 2. MySQL DB 및 TABLE 세팅 (WSL 환경)
MySQL 서비스를 실행 후 make_ros_sql.sql 파일을 이용해 DB와 테이블 생성

```bash
sudo service mysql start
sudo mysql -u root -p < make_ros_sql.sql
```

### 3. 환경 변수(.env) 설정
프로젝트 루트 폴더에 .env.example 파일을 복사해 .env 파일을 생성하고, 본인의 MySQL 비밀번호 입력

```bash
cp .env.example .env
vi .env #pw 입력
```

### 4. 파이썬 가상환경 생성 및 패키지 설치
```bash
python3 -m venv rospyvenv
source rospyvenv/bin/activate
pip install -r requirements.txt
```

### 5. ROS2 패키지 빌드

```bash
cd ~/ros2_study   # 본인의 워크스페이스 경로에 맞게 조정
colcon build --packages-select ros_pkg
source install/setup.bash
```

### 6. 프로그램 실행 (총 3개의 터미널 필요)
터미널 1 (Turtlesim 시뮬레이터 실행)
```bash
ros2 run turtlesim turtlesim_node
```

터미널 2 (C++ ROS2 브릿지 노드 실행)
```bash
cd ~/ros2_study
source install/setup.bash
ros2 run ros_pkg turtle_node
```

터미널 3 (PyQt GUI 실행)
```bash
cd ros-turtle-control
source rospyvenv/bin/activate
python3 gui/app.py
```

# 실행 화면 및 SQL 구성
<img width="514" height="680" alt="image" src="https://github.com/user-attachments/assets/66d3fd81-88a5-408e-8713-bad1764a8dab" />

<img width="501" height="233" alt="스크린샷 2026-09-28 152523" src="https://github.com/user-attachments/assets/d8e87ad2-02d6-4a5a-8cf1-2f97bd153e9f" />


