# prints the mean and standard deviation from last 10s of data
# you must wait 10s before the output starts to print
# pico should be running code from main_acc.py
# Use ctrl + c to stop the code

import serial
import threading
import time
import numpy as np

# Configure the serial port
serial_port = 'COM8'  # Change this to your Pico's serial port
baud_rate = 115200

try:
    ser = serial.Serial(serial_port, baud_rate, timeout=1)  # Add timeout
except serial.SerialException as e:
    print(f"Error opening serial port {serial_port}: {e}")
    exit()

# Buffer to store the last 1000 magnitude readings
buffer_size = 1000
mag_buffer = [0.0] * buffer_size
buffer_index = 0
buffer_filled = False

# Flag to control the reading loop
running = True

# Record the start time
start_time = time.time()

# Function to handle serial data reading
def read_from_serial():
    global buffer_index, buffer_filled
    print("Wait 10s for output")
    while running:
        try:
            line = ser.readline().decode('utf-8').strip()
            if line:
                try:
                    _, _, _, mag = map(float, line.split(','))
                    mag_buffer[buffer_index] = mag
                    buffer_index = (buffer_index + 1) % buffer_size
                    if buffer_index == 0:
                        buffer_filled = True

                    if buffer_filled:
                        avg_mag = np.mean(mag_buffer)
                        std_mag = np.std(mag_buffer)
                        print(f"Average Magnitude: {avg_mag:.5f}, Standard Deviation: {std_mag:.5f}")
                except ValueError:
                    print("Invalid line received")
        except serial.SerialException as e:
            print(f"Serial error: {e}")
            break

# Function to stop the reading loop
def stop_reading():
    global running
    running = False
    time.sleep(1)  # Give some time for the thread to stop
    ser.close()

    # Calculate and print the elapsed time
    elapsed_time = time.time() - start_time
    print(f"Script ran for {elapsed_time:.2f} seconds")

# Start the serial reading thread
thread = threading.Thread(target=read_from_serial)
thread.start()

# Use ctrl + c to stop the code
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    stop_reading()

