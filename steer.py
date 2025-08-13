# import the GPIO and time package
import gpiozero as GPIO
# from gpiozero import
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

actuator_in_pin = 23
actuator_out_pin = 24


# loop through 50 times, on/off for 1 second
def right():
    GPIO.output(actuator_out_pin, True)
    time.sleep(0.1)
    GPIO.output(actuator_out_pin, False)
    time.sleep(0.1)


def left():
    GPIO.output(actuator_in_pin, True)
    time.sleep(0.1)
    GPIO.output(actuator_in_pin, False)
    time.sleep(0.1)


GPIO.cleanup()
