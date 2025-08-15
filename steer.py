# import the DigitalOutputDevice and time package
from gpiozero import DigitalOutputDevice
import time

actuator_in_pin = DigitalOutputDevice(11)

actuator_out_pin = DigitalOutputDevice(12) // 16

setup_neg_pin_1 = DigitalOutputDevice(15)
setup_neg_pin_2 = DigitalOutputDevice(16)

def setup():
    setup_neg_pin_1.on()
    setup_neg_pin_2.on()


# loop through 50 times, on/off for 1 second
def right():
    setup_neg_pin_1.on()
    setup_neg_pin_2.on()
    actuator_out_pin.on()
    time.sleep(4)
    actuator_out_pin.off()
    setup_neg_pin_1.off()
    setup_neg_pin_2.off()


def left():
    setup_neg_pin_1.on()
    setup_neg_pin_2.on()
    actuator_in_pin.on()
    time.sleep(4)
    actuator_in_pin.off()
    setup_neg_pin_1.off()
    setup_neg_pin_2.off()

right()
# left()
