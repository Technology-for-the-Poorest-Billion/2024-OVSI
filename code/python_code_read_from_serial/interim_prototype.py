#this code reads the output from main_interim_prototype.mpy
#it calculates the mean and standard deviation of the last 1000 readings (roughly 10s)
#there is a minimum threshold on the current rolling value of the mean and the standard deviation
#both values must be above the threshold for the screen to turn green, ie oxygen concentrator is on

import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import threading
import time
import numpy as np

# Configure the serial port
serial_port = 'COM8'  # Change this to your serial port
baud_rate = 115200

try:
    ser = serial.Serial(serial_port, baud_rate, timeout=1)  # Add timeout
except serial.SerialException as e:
    print(f"Error opening serial port {serial_port}: {e}")
    exit()

# Initialize data containers
window_size = 200
std_dev_data = deque([0]*window_size, maxlen=window_size)
avg_data = deque([0]*window_size, maxlen=window_size)
mag_buffer = deque([0]*1000, maxlen=1000)

buffer = deque(maxlen=1000)  # Buffer to store incoming data

def read_from_serial():
    while True:
        try:
            line = ser.readline().decode('utf-8').strip()
            if line:
                buffer.append(line)
        except serial.SerialException as e:
            print(f"Serial error: {e}")
            break

# Start the serial reading thread
thread = threading.Thread(target=read_from_serial)
thread.daemon = True
thread.start()

# Initialize the plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
line1, = ax1.plot(range(window_size), std_dev_data, label='Standard Deviation')
line2, = ax2.plot(range(window_size), avg_data, label='Average Magnitude')
ax1.axhline(y=0.02, color='r', linestyle='--', label='Std Dev Threshold')
ax2.axhline(y=0.04, color='r', linestyle='--', label='Average Magnitude Threshold')
ax1.legend(loc='upper left')
ax1.set_ylim(0, 0.1)  # Adjust the limits according to expected std dev range
ax2.legend(loc='upper left')
ax2.set_ylim(0, 0.2)  # Adjust the limits according to your expected mean range

def update(frame):
    while buffer:
        line = buffer.popleft()
        try:
            x, y, z, mag = map(float, line.split(','))
            mag_buffer.append(mag)
            
            if len(mag_buffer) >= 1000:
                std_mag = np.std(mag_buffer)
                avg_mag = np.mean(mag_buffer)
                std_dev_data.append(std_mag)
                avg_data.append(avg_mag)

                line1.set_ydata(std_dev_data)
                line2.set_ydata(avg_data)
                
                # Change background color based on condition
                if avg_mag > 0.04 and std_mag > 0.02:
                    fig.patch.set_facecolor('green')
                else:
                    fig.patch.set_facecolor('red')
        except ValueError:
            print("Invalid line received")
    
    return line1, line2

# Use a higher interval to give the system more time to update
ani = animation.FuncAnimation(fig, update, interval=50)  # Update every 50 ms
plt.show()

# Close the serial port when done
ser.close()
