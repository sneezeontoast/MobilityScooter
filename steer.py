# import the DigitalOutputDevice and time package
from gpiozero import DigitalOutputDevice
import time

# Change colour ones
actuator_in_pin_1 = DigitalOutputDevice(21)  # neg
actuator_in_pin_2 = DigitalOutputDevice(17)  # pos

# Same colour ones
actuator_out_pin_1 = DigitalOutputDevice(16)  # neg
actuator_out_pin_2 = DigitalOutputDevice(18)  # pos

def reset_relays():
    actuator_out_pin_1.off()
    actuator_out_pin_2.off()
    actuator_in_pin_1.off()
    actuator_in_pin_2.off()

# loop through 50 times, on/off for 1 second
def right():
    print("Moving right")
    reset_relays()
    actuator_out_pin_1.on()
    actuator_out_pin_2.on()
    time.sleep(2)
    actuator_out_pin_1.off()
    actuator_out_pin_2.off()
    time.sleep(0.01)


def left():
    print("Moving left yellow wire not reciving")
    reset_relays
    actuator_in_pin_1.on()
    actuator_in_pin_2.on()
    time.sleep(2)
    actuator_in_pin_1.off()
    actuator_in_pin_2.off()
    time.sleep(0.01)

reset_relays()
right()
print("Switching to left")
time.sleep(2)
left()
