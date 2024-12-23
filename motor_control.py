import RPi.GPIO as GPIO
import time

PINS = {
    "enableA": 18, # OUTA 쪽 제어 핀
    "enableB": 19, # OUTB 쪽 제어 핀
    "input1": 23, # 방향 제어 핀 1
    "input2": 24, # 방향 제어 핀 2
    "input3": 25, # 방향 제어 핀 3
    "input4": 26 # 방향 제어 핀 4
}

GPIO.setmode(GPIO.BCM)
for pin in PINS.values():
    GPIO.setup(pin, GPIO.OUT)

PWM_A = GPIO.PWM(PINS["enableA"], 100)
PWM_B = GPIO.PWM(PINS["enableB"], 100)
PWM_A.start(0)
PWM_B.start(0)

def set_motor_speed(side, speed):
    """모터 속도 및 방향 설정"""
    if side == "left":
        GPIO.output(PINS["input1"], GPIO.HIGH if speed > 0 else GPIO.LOW)
        GPIO.output(PINS["input2"], GPIO.LOW if speed > 0 else GPIO.HIGH)
        PWM_A.ChangeDutyCycle(abs(speed))
    elif side == "right":
        GPIO.output(PINS["input3"], GPIO.HIGH if speed > 0 else GPIO.LOW)
        GPIO.output(PINS["input4"], GPIO.LOW if speed > 0 else GPIO.HIGH)
        PWM_B.ChangeDutyCycle(abs(speed))

def cleanup():
    """GPIO 리소스 정리"""
    PWM_A.stop()
    PWM_B.stop()
    GPIO.cleanup()
