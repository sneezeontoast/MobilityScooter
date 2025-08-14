# import the DigitalOutputDevice and time package
from gpiozero import DigitalOutputDevice
import time

actuator_in_pin = DigitalOutputDevice(11)

actuator_out_pin = DigitalOutputDevice(12)


# loop through 50 times, on/off for 1 second
def right():
    actuator_out_pin.on()
    time.sleep(4)
    actuator_out_pin.off()


def left():
    actuator_in_pin.on()
    time.sleep(4)
    actuator_in_pin.on()
