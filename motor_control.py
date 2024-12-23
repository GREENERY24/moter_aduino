import RPi.GPIO as GPIO
import time

PINS = {
    "left": {"input1": 23, "input2": 24},
    "right": {"input1": 27, "input2": 22}
}

GPIO.setmode(GPIO.BCM)
for motor in PINS.values():
    GPIO.setup(motor["input1"], GPIO.OUT)
    GPIO.setup(motor["input2"], GPIO.OUT)

def set_motor_direction(side, direction):
    """모터 방향 설정"""
    if direction == "forward":  # 전진
        GPIO.output(PINS[side]["input1"], GPIO.HIGH)
        GPIO.output(PINS[side]["input2"], GPIO.LOW)
    elif direction == "backward":  # 후진
        GPIO.output(PINS[side]["input1"], GPIO.LOW)
        GPIO.output(PINS[side]["input2"], GPIO.HIGH)
    elif direction == "stop":  # 정지
        GPIO.output(PINS[side]["input1"], GPIO.LOW)
        GPIO.output(PINS[side]["input2"], GPIO.LOW)

def cleanup():
    """GPIO 정리"""
    GPIO.cleanup()
