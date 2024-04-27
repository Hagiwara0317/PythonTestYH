from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

def main_loop():
    num = 0
    while num < 10:
        GPIO.output(18,GPIO.HIGH)
        sleep(1)
        GPIO.output(18,GPIO.LOW)
        sleep(1)
        num += 1

if __name__ == '__main__':
    main_loop()
