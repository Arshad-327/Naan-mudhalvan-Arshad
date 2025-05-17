import RPi.GPIO as GPIO

LEFT_MOTOR = 17
RIGHT_MOTOR = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEFT_MOTOR, GPIO.OUT)
GPIO.setup(RIGHT_MOTOR, GPIO.OUT)

def move_forward():
    GPIO.output(LEFT_MOTOR, True)
    GPIO.output(RIGHT_MOTOR, True)

def stop():
    GPIO.output(LEFT_MOTOR, False)
    GPIO.output(RIGHT_MOTOR, False)