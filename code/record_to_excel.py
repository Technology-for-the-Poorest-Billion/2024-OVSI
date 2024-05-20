#prints readings live and save results to excel
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

# Function to handle serial data reading
def read_from_serial():
    while running:
        try:
            line = ser.readline().decode('utf-8').strip()
            if line:
                try:
                    x, y, z, mag = map(float, line.split(','))
                    print(f"X: {x:.2f}, Y: {y:.2f}, Z: {z:.2f}, Magnitude: {mag:.2f}")
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

# Start the serial reading thread
thread = threading.Thread(target=read_from_serial)
thread.start()

# Wait for user input to stop the script
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    stop_reading()

# use ctrl + c to stop the code