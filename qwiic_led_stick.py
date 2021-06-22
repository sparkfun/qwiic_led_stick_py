#-----------------------------------------------------------------------------
# qwiic_led_stick.py
#
# Python library for the SparkFun Qwiic LED Stick - APA102C.
#   https://www.sparkfun.com/products/18354
#
#------------------------------------------------------------------------
#
# Written by Priyanka Makin @ SparkFun Electronics, June 2021
# 
# This python library supports the SparkFun Electroncis qwiic 
# qwiic sensor/board ecosystem 
#
# More information on qwiic is at https:// www.sparkfun.com/qwiic
#
# Do you like this library? Help support SparkFun. Buy a board!
#==================================================================================
# Copyright (c) 2020 SparkFun Electronics
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.
#==================================================================================

"""
qwiic_led_stick
===============
Python module for the SparkFun Qwiic LED Stick - APA102C.

This package is a port of the existing [SparkFun Qwiic LED Stick Arduino Library](https://github.com/sparkfun/SparkFun_Qwiic_LED_Stick_Arduino_Library).

This package can be used in conjunction with the overall [SparkFun Qwiic Python Package](https://github.com/sparkfun/Qwiic_Py).

New to qwiic? Take a look at the entire [SparkFun Qwiic Ecoststem](https://www.sparkfun.com/qwiic).
"""
# ---------------------------------------------------------------------------------

import math
import time
import qwiic_i2c

_DEFAULT_NAME = "Qwiic LED Stick"

_QWIIC_LED_STICK_DEFAULT_ADDRESS = 0x23
_FULL_ADDRESS_LIST = list(range(0x08, 0x77+1)) # Full address list (excluding reserved addresses)
_FULL_ADDRESS_LIST.remove(_QWIIC_LED_STICK_DEFAULT_ADDRESS >> 1) # Remove default address from list
_AVAILABLE_I2C_ADDRESS = [_QWIIC_LED_STICK_DEFAULT_ADDRESS] # Initialize with default address
_AVAILABLE_I2C_ADDRESS.extend(_FULL_ADDRESS_LIST) # Add full range of I2C addresses

class QwiicLEDStick(object):
    """
    QwiicLEDStick

        :param address: The I2C address to use for the device.
                        If not provided, the default address is used.
        :param i2c_driver: An existing i2c driver object. If not provided a 
                        a driver is created.
        :return: The GPIO device object.
        :rtype: Object
    """
    # Constructor
    device_name = _DEFAULT_NAME
    available_addresses = _AVAILABLE_I2C_ADDRESS

    # Qwiic LED Stick commands
    COMMAND_CHANGE_ADDRESS = 0xC7
    COMMAND_CHANGE_LED_LENGTH = 0x70
    COMMAND_WRITE_SINGLE_LED_COLOR = 0x71
    COMMAND_WRITE_ALL_LED_COLOR = 0x72
    COMMAND_WRITE_RED_ARRAY = 0x73
    COMMAND_WRITE_GREEN_ARRAY = 0x74
    COMMAND_WRITE_BLUE_ARRAY = 0x75
    COMMAND_WRITE_SINGLE_LED_BRIGHTNESS = 0x76
    COMMAND_WRITE_ALL_LED_BRIGHTNESS = 0x77
    COMMAND_WRITE_ALL_LED_OFF = 0x78

    def __init__(self, address=None, i2c_driver=None):

        # Did the user specify an I2C address?
        self.address = address if address != None else self.available_addresses[0]

        # Load the I2C driver if one isn't provided
        if i2c_driver == None:
            self._i2c = qwiic_i2c.getI2CDriver()
            if self._i2c == None:
                print("Unable to load I2C driver for this platform.")
                return
        else:
            self._i2c = i2c_driver
    
    # ------------------------------------------------------------------------------
    # is_connected()
    #
    # Is an actual board connected to our system?
    def is_connected(self):
        """
            Determine if a Qwiic SGP40 device is connected to the system.

            :return: True if the device is connected, false otherwise.
            :rtype: bool
        """
        return qwiic_i2c.isDeviceConnected(self.address)

    # ------------------------------------------------------------------------------
    # begin()
    #
    # Initialize the system and validate the board.
    def begin(self):
        """
            Initialize the operation of the Qwiic LED Stick.
            Run is_connected()

            :return: Returns true if an LED Stick is connected to the system
                    False otherwise.
            :rtype: bool
        """
        return self.is_connected()
    
    # ------------------------------------------------------------------------------
    # set_single_LED_color(number, red, green, blue)
    #
    # Change the color of a specific LED.
    def set_single_LED_color(self, number, red, green, blue):
        """
            Change the color of a specific LED.
            Each color must be a value between 0-255.
            LED indexed starting at 1.

            :return: Returns true if command written successfully, false otherwise
            :rtype: bool
        """
        # TODO: do I need to do some boundary checking here?
        data = [number, red, green, blue]
        return self._i2c.writeBlock(self.address, self.COMMAND_WRITE_SINGLE_LED_COLOR, data)

    # ------------------------------------------------------------------------------
    # set_all_LED_color(red, green, blue)
    #
    # Set the color of all LEDs in the string
    def set_all_LED_color(self, red, green, blue):
        """
            Set the color of all LEDs in the string. Each will be shining the same color.
            The color value must be between 0-255.

            :return: Returns true if command is written successfully, false otherwise
            :rtype: bool
        """
        data = [red, green, blue]
        return self._i2c.writeBlock(self.address, self.COMMAND_WRITE_ALL_LED_COLOR, data)
    