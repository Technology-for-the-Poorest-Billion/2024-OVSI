# shows a live 3d plot with the last 200 rolling data points plotted
# shows accelerometer mean and std and microphone mean
# planes can be edited to show any chosen threshold value


import serial
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from collections import deque
import threading
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
mic_avg_data = deque([0]*window_size, maxlen=window_size)
mag_buffer = deque([0]*1000, maxlen=1000)
mic_buffer = deque([0]*1000, maxlen=1000)

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
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Data placeholders for 3D scatter plot
xs, ys, zs = deque([0]*window_size, maxlen=window_size), deque([0]*window_size, maxlen=window_size), deque([0]*window_size, maxlen=window_size)

sc = ax.scatter(xs, ys, zs, c='b', marker='o')
ax.set_xlabel('Standard Deviation')
ax.set_ylabel('Average Magnitude')
ax.set_zlabel('Microphone Mean Magnitude')
ax.set_xlim(0, 0.1)
ax.set_ylim(0, 0.2)
ax.set_zlim(0, 2)

std_threshold = 0.02
avg_threshold = 0.04
mic_threshold = 1.4

# Define grid for threshold planes
x = np.linspace(0, 0.1, 10)
y = np.linspace(0, 0.2, 10)
z = np.linspace(0, 2, 10)

# Create meshgrid for planes
Y, Z = np.meshgrid(y, z)
X1, Z1 = np.meshgrid(x, z)
X2, Y2 = np.meshgrid(x, y)

# Plot threshold planes
ax.plot_surface(np.full_like(Y, std_threshold), Y, Z, alpha=0.3, color='r')  # Plane at x = 0.02
ax.plot_surface(X1, np.full_like(X1, avg_threshold), Z1, alpha=0.3, color='g')  # Plane at y = 0.04
ax.plot_surface(X2, Y2, np.full_like(X2, mic_threshold), alpha=0.3, color='b')  # Plane at z = 1.4

def update(frame):
    while buffer:
        line = buffer.popleft()
        try:
            mag, vu_value = map(float, line.split(','))
            mag_buffer.append(mag)
            mic_buffer.append(vu_value)
            
            if len(mag_buffer) >= 1000:
                std_mag = np.std(mag_buffer)
                avg_mag = np.mean(mag_buffer)
                mic_mean = np.mean(mic_buffer)
                
                std_dev_data.append(std_mag)
                avg_data.append(avg_mag)
                mic_avg_data.append(mic_mean)
                
                # Update 3D plot data
                xs.append(std_mag)
                ys.append(avg_mag)
                zs.append(mic_mean)

                sc._offsets3d = (xs, ys, zs)
                
                # Change background color based on condition
                if avg_mag > avg_threshold and std_mag > std_threshold and mic_mean > mic_threshold:
                    fig.patch.set_facecolor('green')
                else:
                    fig.patch.set_facecolor('red')
        except ValueError:
            print("Invalid line received")
    
    return sc,

# Use a higher interval to give the system more time to update
ani = animation.FuncAnimation(fig, update, interval=50)  # Update every 50 ms
plt.show()

# Close the serial port when done
ser.close()
