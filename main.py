# <<<<<<!!!!!!!! Mobility scooter Vo2 Code !!!!!!!>>>>>>>>

# RUN THIS:
# sudo pip3 install bluedot

from bluedot import BlueDot
from signal import pause
import steer
import potentiometer as p

forward = 15.27
backwards = 2
stop = 7.17 #  maybe 9.17

moving = False
def dpad(pos):
    if pos.top:
        # Start
        print("up")
        p.set_voltage(forward)
    elif pos.bottom:
        # Brake

        print("Back")
        p.set_voltage(backwards)
    elif pos.left:

        # Turn Left
        print("left")
        steer.left()
    elif pos.right:
        # Turn right
        print("right")
        steer.right()
    elif pos.middle:

        print("Stop ••••|")
        p.set_voltage(stop)

bd = BlueDot()
while True:
    bd.when_pressed = dpad


pause()
