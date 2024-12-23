import json
from navigation import rotate, move_forward
from sensor import get_distance
import math

# 위치 데이터
with open("positions.json", "r") as f:
    positions = json.load(f)
    
def navigate_to(target):
    """목표 위치로 이동"""
    current_position = {"x": 0, "y": 0}  # 초기위치 설정
    target_position = positions[target]

    dx = target_position["x"] - current_position["x"]
    dy = target_position["y"] - current_position["y"]
    angle = math.degrees(math.atan2(dy, dx))

    print(f"Turning to {angle} degrees...")
    rotate(angle)

    distance = math.sqrt(dx**2 + dy**2)
    print(f"Moving forward {distance} cm...")
    move_forward(distance)

if __name__ == "__main__":
    target = input("Enter target location: ")
    if target in positions:
        navigate_to(target)
    else:
        print("Invalid target location.")
