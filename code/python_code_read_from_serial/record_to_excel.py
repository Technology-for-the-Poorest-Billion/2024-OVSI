#prints readings live and save results to excel from main_interim_prototype.mpy
#use ctrl + c to save to excel and stop code

import serial
import pandas as pd
import threading
import time

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

# Flag to control the reading loop
running = True

# Record the start time
start_time = time.time()

# Function to handle serial data reading
def read_from_serial():
    while running:
        try:
            line = ser.readline().decode('utf-8').strip()
            if line:
                try:
                    x, y, z, mag = map(float, line.split(','))
                    print(f"X: {x:.3f}, Y: {y:.3f}, Z: {z:.3f}, Magnitude: {mag:.3f}")
                    data.append({'X': x, 'Y': y, 'Z': z, 'Magnitude': mag})
                except ValueError:
                    print("Invalid line received")
        except serial.SerialException as e:
            print(f"Serial error: {e}")
            break

# Function to save data to an Excel file
def save_to_excel(data, filename='output.xlsx'):
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

# Use ctrl + c to stop the code
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    stop_reading()

