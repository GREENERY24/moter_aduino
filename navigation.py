from motor_control import set_motor_speed
import time

def rotate(angle):
    """로봇 회전"""
    turn_time = abs(angle) / 90
    if angle > 0:
        set_motor_speed("left", 50)
        set_motor_speed("right", -50)
    elif angle < 0:
        set_motor_speed("left", -50)
        set_motor_speed("right", 50)
    
    time.sleep(turn_time)
    set_motor_speed("left", 0)
    set_motor_speed("right", 0)

def move_forward(distance):
    """직진"""
    travel_time = distance / 20
    set_motor_speed("left", 50)
    set_motor_speed("right", 50)
    time.sleep(travel_time)
    set_motor_speed("left", 0)
    set_motor_speed("right", 0)
