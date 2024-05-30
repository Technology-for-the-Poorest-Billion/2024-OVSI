# this code prints the output from the pico when running the code main_mic.py

import serial

# Configure the serial port
serial_port = 'COM8'  # Change this to your Pico's serial port
baud_rate = 115200

try:
    ser = serial.Serial(serial_port, baud_rate, timeout=1)  # Add timeout
except serial.SerialException as e:
    print(f"Error opening serial port {serial_port}: {e}")
    exit()

while True:
    try:
        line = ser.readline().decode('utf-8').strip()
        print(f"Received line: {line}")
    except serial.SerialException as e:
        print(f"Serial error: {e}")
        break

# Close the serial port when done
ser.close()