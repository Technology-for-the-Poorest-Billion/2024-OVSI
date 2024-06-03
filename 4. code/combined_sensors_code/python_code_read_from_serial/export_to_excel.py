# records the accelerometer mean and std on a 10s rolling average
# records the microphone volume units on a 10s rolling average
# saves these in an excel file
# currently records 6000 readings but this can be adjusted
# the first 10s does not record any data as the rolling data measures
# do not have enough information to calculate it yet

import serial
import pandas as pd
import threading
import time
import numpy as np
from collections import deque

# Configure the serial port
serial_port = 'COM8'  # Change this to your Pico's serial port
baud_rate = 115200

try:
    ser = serial.Serial(serial_port, baud_rate, timeout=1)  # Add timeout
except serial.SerialException as e:
    print(f"Error opening serial port {serial_port}: {e}")
    exit()

# List to store the data
data = []

# Buffers to calculate mean and std dev
mag_buffer = deque(maxlen=1000)
mic_buffer = deque(maxlen=1000)

# Flag to control the reading loop
running = True

# Record the start time
start_time = time.time()

# Function to handle serial data reading
def read_from_serial():
    # edit to control how many readings are taken
    while running and len(data) < 6000:
        try:
            line = ser.readline().decode('utf-8').strip()
            if line:
                try:
                    mag, vu_value = map(float, line.split(','))
                    mag_buffer.append(mag)
                    mic_buffer.append(vu_value)
                    
                    if len(mag_buffer) == 1000:
                        print(len(data))
                        std_mag = np.std(mag_buffer)
                        avg_mag = np.mean(mag_buffer)
                        mic_mean = np.mean(mic_buffer)
                        
                        data.append({
                            'Mean Magnitude': avg_mag,
                            'Standard Deviation': std_mag,
                            'Microphone Output': mic_mean
                        })
                        
                        if len(data) >= 6000:
                            stop_reading()
                            
                except ValueError:
                    print("Invalid line received")
        except serial.SerialException as e:
            print(f"Serial error: {e}")
            break

# Function to save data to an Excel file
def save_to_excel(data, filename='3_output_random_noise.xlsx'):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

# Function to stop the reading loop and save data
def stop_reading():
    global running
    running = False
    time.sleep(1)  # Give some time for the thread to stop
    print("Exiting and saving data to Excel...")
    save_to_excel(data)
    ser.close()
    print("Data saved to output.xlsx")

    # Calculate and print the elapsed time
    elapsed_time = time.time() - start_time
    print(f"Script ran for {elapsed_time:.2f} seconds")

# Start the serial reading thread
thread = threading.Thread(target=read_from_serial)
thread.start()

# Wait for user input to stop the script
try:
    while len(data) < 6000:
        time.sleep(1)
except KeyboardInterrupt:
    stop_reading()

# Use ctrl + c to stop the code
