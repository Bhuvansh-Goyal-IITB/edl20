import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if not GPIO.input(15):
            GPIO.output(14, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(14, GPIO.LOW)
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
