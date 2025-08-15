# import the DigitalOutputDevice and time package
from gpiozero import DigitalOutputDevice
import time

# Change colour ones
actuator_in_pin_1 = DigitalOutputDevice(18)  # neg
actuator_in_pin_2 = DigitalOutputDevice(23)  # pos

# Same colour ones
actuator_out_pin_1 = DigitalOutputDevice(22)  # neg
actuator_out_pin_2 = DigitalOutputDevice(17)  # pos


# loop through 50 times, on/off for 1 second
def right():
    print("Moving right")

    actuator_out_pin_1.on()
    actuator_out_pin_2.on()
    time.sleep(4)
    actuator_out_pin_1.off()
    actuator_out_pin_2.off()


def left():
    print("Moving left")
    actuator_in_pin_1.on()
    actuator_in_pin_2.on()
    time.sleep(4)
    actuator_in_pin_1.off()
    actuator_in_pin_2.off()


right()
left()
