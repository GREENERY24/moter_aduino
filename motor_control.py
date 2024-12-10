import RPi.GPIO as GPIO
import time

# 모터 드라이버 핀 설정이임
PINS = {
    "left": {"enable": 18, "input1": 23, "input2": 24},
    "right": {"enable": 17, "input1": 27, "input2": 22}
}

GPIO.setmode(GPIO.BCM)
for motor in PINS.values():
    GPIO.setup(motor["enable"], GPIO.OUT)
    GPIO.setup(motor["input1"], GPIO.OUT)
    GPIO.setup(motor["input2"], GPIO.OUT)

# PWM 설정
PWM = {
    "left": GPIO.PWM(PINS["left"]["enable"], 100),
    "right": GPIO.PWM(PINS["right"]["enable"], 100)
}
PWM["left"].start(0)
PWM["right"].start(0)

def set_motor_speed(side, speed):
    """모터 속도 설정"""
    if speed > 0:
        GPIO.output(PINS[side]["input1"], GPIO.HIGH)
        GPIO.output(PINS[side]["input2"], GPIO.LOW)
    elif speed < 0:
        GPIO.output(PINS[side]["input1"], GPIO.LOW)
        GPIO.output(PINS[side]["input2"], GPIO.HIGH)
    else:
        GPIO.output(PINS[side]["input1"], GPIO.LOW)
        GPIO.output(PINS[side]["input2"], GPIO.LOW)

    PWM[side].ChangeDutyCycle(abs(speed))

def cleanup():
    "GPIO 정리"
    for pwm in PWM.values():
        pwm.stop()
    GPIO.cleanup()
