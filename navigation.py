import time
from motor_control import set_motor_direction

def rotate(angle):
    """주어진 각도로 로봇 회전"""
    if angle > 0:  # 우회전 (오른쪽으로 회전)
        set_motor_direction("left", "forward")   # 왼쪽 바퀴만 전진
        set_motor_direction("right", "stop")     # 오른쪽 바퀴는 멈춤
    elif angle < 0:  # 좌회전 (왼쪽으로 회전)
        set_motor_direction("left", "stop")      # 왼쪽 바퀴는 멈춤
        set_motor_direction("right", "forward")  # 오른쪽 바퀴만 전진

    time.sleep(abs(angle) / 90)  # 90도 회전하는 데 필요한 시간
    set_motor_direction("left", "stop")
    set_motor_direction("right", "stop")

def move_forward(distance):
    """주어진 거리만큼 직진"""
    set_motor_direction("left", "forward")
    set_motor_direction("right", "forward")
    time.sleep(distance / 10)  # 거리와 속도에 따른 시간 계산
    set_motor_direction("left", "stop")
    set_motor_direction("right", "stop")
