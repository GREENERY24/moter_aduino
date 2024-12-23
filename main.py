import json
from navigation import rotate, move_forward
from sensor import get_distance
import math

# 위치 데이터
with open("positions.json", "r") as f:
    positions = json.load(f)

def navigate_to(target):
    """목표 위치로 이동"""
    current_position = {"x": 0, "y": 0}  # 초기 위치
    target_position = positions[target]

    dx = target_position["x"] - current_position["x"]
    dy = target_position["y"] - current_position["y"]
    angle = math.degrees(math.atan2(dy, dx))

    rotate(angle)
    distance = math.sqrt(dx**2 + dy**2)
    move_forward(distance)

def avoid_obstacles():
    """장애물 피하기"""
    while True:
        distance = get_distance()
        if distance < 20:  # 20cm 이내에 장애물이 있으면 회전
            rotate(90)  # 우회전 (90도 회전)
        else:
            move_forward(10)  # 일정 거리만큼 전진

if __name__ == "__main__":
    target = input("Enter target location: ")
    navigate_to(target)
    avoid_obstacles()
