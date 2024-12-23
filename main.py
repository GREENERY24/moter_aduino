import json
from navigation import rotate, move_forward
import math

# 위치 데이터
with open("positions.json", "r") as f:
    positions = json.load(f)

def navigate_to(target):
    "목표 위치로 이동"
    current_position = {"x": 0, "y": 0}  # 초기 위치
    target_position = positions[target]

    dx = target_position["x"] - current_position["x"]
    dy = target_position["y"] - current_position["y"]
    angle = math.degrees(math.atan2(dy, dx))

    rotate(angle)  # 목표 방향으로 회전
    distance = math.sqrt(dx**2 + dy**2)
    move_forward(distance)  # 목표 위치로 이동

if __name__ == "__main__":
    target = input("Enter target location: ")
    navigate_to(target)
