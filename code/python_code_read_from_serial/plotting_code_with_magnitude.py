# code for plotting x, y, z components and magnitude using a buffer
# pico must be using code from main_interim_prototype.mpy

import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import threading
import time

# Configure the serial port
serial_port = 'COM8'
baud_rate = 115200

try:
    ser = serial.Serial(serial_port, baud_rate, timeout=1) 
except serial.SerialException as e:
    print(f"Error opening serial port {serial_port}: {e}")
    exit()

# Initialize data containers
window_size = 200
x_data = deque([0]*window_size, maxlen=window_size)
y_data = deque([0]*window_size, maxlen=window_size)
z_data = deque([0]*window_size, maxlen=window_size)
mag_data = deque([0]*window_size, maxlen=window_size)

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
line1, = ax1.plot(range(window_size), x_data, label='X')
line2, = ax1.plot(range(window_size), y_data, label='Y')
line3, = ax1.plot(range(window_size), z_data, label='Z')
line4, = ax2.plot(range(window_size), mag_data, label='Magnitude')
ax1.legend(loc='upper left')
ax1.set_ylim(-2, 2)  # Adjust the limits according to your FSR settings
ax2.legend(loc='upper left')
ax2.set_ylim(0, 2)  # Adjust the limits according to your expected magnitude range

def update(frame):
    while buffer:
        line = buffer.popleft()
        try:
            x, y, z, mag = map(float, line.split(','))
            x_data.append(x)
            y_data.append(y)
            z_data.append(z)
            mag_data.append(mag)

            line1.set_ydata(x_data)
            line2.set_ydata(y_data)
            line3.set_ydata(z_data)
            line4.set_ydata(mag_data)
        except ValueError:
            print("Invalid line received")
    
    return line1, line2, line3, line4

# Use a higher interval to give the system more time to update
ani = animation.FuncAnimation(fig, update, interval=50)  # Updates every 50 ms
plt.show()

# Close the serial port when done
ser.close()
