import RPi.GPIO as GPIO
import time

TRIG = 5
ECHO = 6

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    """초음파 센서를 사용하여 거리 측정"""
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)

    while GPIO.input(ECHO) == GPIO.LOW:
        start_time = time.time()
    while GPIO.input(ECHO) == GPIO.HIGH:
        end_time = time.time()

    duration = end_time - start_time
    return (duration * 34300) / 2  # cm
