# import the DigitalOutputDevice and time package
from gpiozero import DigitalOutputDevice
import time

# Change colour ones
actuator_in_pin_1 = DigitalOutputDevice(27)  # neg green
actuator_in_pin_2 = DigitalOutputDevice(15)  # pos yellow

# Same colour ones
actuator_out_pin_1 = DigitalOutputDevice(21)  # neg orange
actuator_out_pin_2 = DigitalOutputDevice(17)  # pos white wire


# loop through 50 times, on/off for 1 second
def right():
    print("Moving right")

    actuator_out_pin_1.on()
    actuator_out_pin_2.on()
    time.sleep(2)
    actuator_out_pin_1.off()
    actuator_out_pin_2.off()


def left():
    print("Moving left")
    actuator_in_pin_1.on()
    actuator_in_pin_2.on()
    time.sleep(2)
    actuator_in_pin_1.off()
    actuator_in_pin_2.off()


right()
time.sleep(2)
left()
