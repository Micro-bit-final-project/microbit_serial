## Micro:bit Serial module
This repository contains a python module used to communicate via serial with a Micro:bit. This module is used by every python script that relies on Micro:bit input in this organisation.

### Set up
Make sure you are running python 3. This software has been tested on python 3.8.6. You also need to install pyserial and pygame. Pygame is not a direct dependency of this script, but other scripts in this organisation rely on pygame.
### Repo structure
* [microbit_serial.py](https://github.com/Micro-bit-final-project/microbit_serial/blob/master/microbit_serial.py "microbit_serial.py"): Python script that provides functions to connect to, receive and parse data from a Micro:bit using serial.
