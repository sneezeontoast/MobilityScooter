# <<<<<<!!!!!!!! Mobility scooter Vo2 Code !!!!!!!>>>>>>>>

# RUN THIS:
# sudo pip3 install bluedot

from bluedot import BlueDot
from signal import pause
import steer
import potentiometer

def dpad(pos):
    if pos.top:
        # Start
        print("up")
    elif pos.bottom:
        # Brake
        print("Stop ••••|")
    elif pos.left:

        # Turn Left
        print("left")
    elif pos.right:
        # Turn right
        print("right")
    elif pos.middle:
        # nothing
        print("nothing yet...")

bd = BlueDot()
bd.when_pressed = dpad

pause()
