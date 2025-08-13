# <<<<<<!!!!!!!! Mobility scooter Vo2 Code !!!!!!!>>>>>>>>

# RUN THIS:
# sudo pip3 install bluedot

from bluedot import BlueDot
from signal import pause
import steer
import potentiometer as p

def dpad(pos):
    if pos.top:
        # Start
        print("up")
        p.set_voltage(9)
    elif pos.bottom:
        # Brake

        print("Stop ••••|")
        p.set_voltage(0)
    elif pos.left:

        # Turn Left
        print("left")
        steer.left()
    elif pos.right:
        # Turn right
        print("right")
        steer.right()
    elif pos.middle:
        # nothing
        print("nothing yet...")

bd = BlueDot()
while True:
    bd.when_pressed = dpad


pause()
