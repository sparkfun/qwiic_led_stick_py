Qwiic_LED_Stick_Py
===============

<p align="center">
   <img src="https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo-registered.jpg"  width=200>  
   <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"  width=240>   
</p>
<p align="center">
	<a href="https://pypi.org/project/sparkfun-qwiic-led-stick/" alt="Package">
		<img src="https://img.shields.io/pypi/pyversions/sparkfun-qwiic-led-stick.svg" /></a>
	<a href="https://github.com/sparkfun/Qwiic_LED_Stick_Py/issues" alt="Issues">
		<img src="https://img.shields.io/github/issues/sparkfun/Qwiic_LED_Stick_Py.svg" /></a>
	<a href="https://qwiic-led-stick-py.readthedocs.io/en/latest/?" alt="Documentation">
		<img src="https://readthedocs.org/projects/qwiic-led-stick-py/badge/?version=latest&style=flat" /></a>
	<a href="https://github.com/sparkfun/Qwiic_LED_Stick_Py/blob/master/LICENSE" alt="License">
		<img src="https://img.shields.io/badge/license-MIT-blue.svg" /></a>
	<a href="https://twitter.com/intent/follow?screen_name=sparkfun">
        	<img src="https://img.shields.io/twitter/follow/sparkfun.svg?style=social&logo=twitter"
           	 alt="follow on Twitter"></a>

</p>

<img src="https://cdn.sparkfun.com/assets/parts/1/7/6/9/9/18354-SparkFun_Qwiic_LED_Stick_-_APA102C-01.jpg"  align="right" width=300 alt="SparkFun Qwiic LED Stick">

Python module for the [SparkFun Qwiic LED Stick - APA102C](https://www.sparkfun.com/products/18354)

This python package is a port of the existing [SparkFun Qwiic LED Stick Arduino Library](https://github.com/sparkfun/SparkFun_Qwiic_LED_Stick_Arduino_Library)

This package can be used in conjunction with the overall [SparkFun qwiic Python Package](https://github.com/sparkfun/Qwiic_Py)

New to qwiic? Take a look at the entire [SparkFun qwiic ecosystem](https://www.sparkfun.com/qwiic).

## Contents

* [Supported Platforms](#supported-platforms)
* [Dependencies](#dependencies)
* [Installation](#installation)
* [Documentation](#documentation)
* [Example Use](#example-use)

Supported Platforms
--------------------
The Qwiic LED Stick Python package currently supports the following platforms:
* [Raspberry Pi](https://www.sparkfun.com/search/results?term=raspberry+pi)

Dependencies
--------------
This driver package depends on the qwiic I2C driver:
[Qwiic_I2C_Py](https://github.com/sparkfun/Qwiic_I2C_Py)

Documentation
-------------
The SparkFun Qwiic LED Stick module documentation is hosted at [ReadTheDocs](https://qwiic-led-stick-py.readthedocs.io/en/latest/?)

Installation
---------------
### PyPi Installation

This repository is hosted on PyPi as the [sparkfun-qwiic-led-stick](https://pypi.org/project/sparkfun-qwiic-led-stick/) package. On systems that support PyPi installation via pip, this library is installed using the following commands

For all users (note: the user must have sudo privileges):
```sh
sudo pip install sparkfun-qwiic-led-stick
```
For the current user:

```sh
pip install sparkfun-qwiic-led-stick
```
To install, make sure the setuptools package is installed on the system.

Direct installation at the command line:
```sh
python setup.py install
```

To build a package for use with pip:
```sh
python setup.py sdist
 ```
A package file is built and placed in a subdirectory called dist. This package file can be installed using pip.
```sh
cd dist
pip install sparkfun-qwiic-led-stick-<version>.tar.gz
```

Example Use
 -------------
See the examples directory for more detailed use examples.

```python
from __future__ import print_function
import qwiic_led_stick
import time
import sys

def run_example():

    print("\nSparkFun Qwiic LED Stick Example 1")
    my_stick = qwiic_led_stick.QwiicLEDStick()

    if my_stick.begin() == False:
        print("\nThe Qwiic LED Stick isn't connected to the sytsem. Please check your connection", \
            file=sys.stderr)
        return
    print("\nLED Stick ready!")
    
    my_stick.set_all_LED_brightness(15)

    while True:
        
        # Turn on all the LEDs to white
        my_stick.set_all_LED_color(50, 50, 50)
        time.sleep(1)
        # Turn off all LEDs
        my_stick.LED_off()
        time.sleep(1)

if __name__ == '__main__':
    try:
        run_example()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)
```
<p align="center">
<img src="https://cdn.sparkfun.com/assets/custom_pages/3/3/4/dark-logo-red-flame.png" alt="SparkFun - Start Something">
</p>
