# attempts to print the serial output from main_acc.py
# has extra tests to try and find any errors

import serial

# Configure the serial port
serial_port = 'COM8'  # Change this to your Pico's serial port
baud_rate = 115200

try:
    ser = serial.Serial(serial_port, baud_rate, timeout=1)  # Add timeout
except serial.SerialException as e:
    print(f"Error opening serial port {serial_port}: {e}")
    exit()

def read_from_serial():
    while True:
        try:
            line = ser.readline().decode('utf-8').strip()
            if line:
                try:
                    x, y, z, mag = map(float, line.split(','))
                    print(f"X: {x:.3f}, Y: {y:.3f}, Z: {z:.3f}, Magnitude: {mag:.3f}")
                except ValueError:
                    print("Invalid line received")
        except serial.SerialException as e:
            print(f"Serial error: {e}")
            break

# Read and print serial data
read_from_serial()

# Close the serial port when done
ser.close()