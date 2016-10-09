# python-gamepad-keyboard

# Introduction

You have to install the [corresponding sketch](https://github.com/thomas-rager/serial-arduino-gamepad) on your Arduino UNO or compatible.
The Arduino will send all keypresses over the serial-interface and this script will
emulate a keyboard to make the gamepad usabel under linux.

## Installation
    sudo apt-get install python-pip
    sudo pip install python-uinput
    sudo pip install pyserial

## Execute
Run `sudo python gamepad.py` form the commandline.
If you want to use the joystick you need to run it on startup.
See `/etc/rc.local`.

You may have to adapt the serial-interface in line 4 of `gamepad.py` to your needs.  

---

Author: Thomas Rager

