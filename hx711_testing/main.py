import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.OUT, initial=GPIO.HIGH)

time.sleep(1)

GPIO.output(6, GPIO.LOW)

try:
    while True:
        # DT will be high untill the adc is ready
        # val_count = 0
        # avg = 0
            
        while GPIO.input(5):
            pass
        
        value = 0
        for i in range(0, 24):
            GPIO.output(6, GPIO.HIGH)
            GPIO.output(6, GPIO.LOW)

            value = value | GPIO.input(5)
            if i != 23:
                value = value << 1

        GPIO.output(6, GPIO.HIGH)
        GPIO.output(6, GPIO.LOW)

        if value & (1 << 23):
            value -= (1 << 24)
        print(value)
except KeyboardInterrupt:
    GPIO.cleanup()
        

