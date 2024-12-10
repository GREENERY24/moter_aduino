import math
from motor_control import set_motor_speed
import time

def rotate(angle):
    "주어진 각도로 로봇 회전"
    if angle > 0:
        set_motor_speed("left", 50)
        set_motor_speed("right", -50)
    elif angle < 0:
        set_motor_speed("left", -50)
        set_motor_speed("right", 50)

    time.sleep(abs(angle) / 90) # 90도 회전에 필요한 시간
    set_motor_speed("left", 0)
    set_motor_speed("right", 0)

def move_forward(distance):
    "주어진 거리만큼 직진"
    set_motor_speed("left", 50)
    set_motor_speed("right", 50)
    time.sleep(distance / 10) # 거리와 속도에 따른 시간 계산
    set_motor_speed("left", 0)
    set_motor_speed("right", 0)
    