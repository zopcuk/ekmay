import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# Setup GPIO Pins
GPIO.setup(12, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
# Set PWM instance and their frequency
pwm12 = GPIO.PWM(12, 60)
pwm32 = GPIO.PWM(32, 60)
pwm33 = GPIO.PWM(33, 60)
pwm35 = GPIO.PWM(35, 60)
# Start PWM with 50% Duty Cycle
pwm12.start(0)
pwm32.start(0)
pwm33.start(0)
pwm35.start(0)
a = 0
try:
	while True:
		for dutyCycle in range (0, 100, 5):
			pwm12.ChangeDutyCycle(dutyCycle)
			pwm32.ChangeDutyCycle(100-dutyCycle)
			pwm33.ChangeDutyCycle(dutyCycle)
			pwm35.ChangeDutyCycle(100-dutyCycle)
			time.sleep(0.1)
		for dutyCycle in range (100, 0, -5):
			pwm12.ChangeDutyCycle(dutyCycle)
			pwm32.ChangeDutyCycle(100-dutyCycle)
			pwm33.ChangeDutyCycle(dutyCycle)
			pwm35.ChangeDutyCycle(100-dutyCycle)
			time.sleep(0.1)
except KeyboardInterrupt:
	pwm12.stop()
	pwm32.stop()
	pwm33.stop()
	pwm35.stop()
# Cleans the GPIO
GPIO.cleanup()