# Final Prototype Code

This folder contains the code needed to run the final prototype.

`main_combined_sensors.py` contains the micropython code that is used on the Raspberry Pi Pico to take the accelerometer output, and convert it into the accelerometer magnitude. It also takes the analogue microphone signal and converts it into a noise reading on a scale of 1-10.

`final_prototype.py` contains the python code to be used on a laptop to read the Pi Pico output through the serial port. There is a description of the code functionality at the top of the code.

The circuit needed to run the code is shown in the `hardware_and_circuitry.md` file.
