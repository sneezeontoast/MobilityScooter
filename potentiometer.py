# Do this first:
#sudo pip3 install adafruit-circuitpython-ds3502

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board

import adafruit_ds3502

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
ds3502 = adafruit_ds3502.DS3502(i2c)

# As this code runs, measure the voltage between ground and the RW (wiper) pin
# with a multimeter. You should see the voltage change with each print statement.


def set_voltage(vol):
    ds3502.wiper = vol


