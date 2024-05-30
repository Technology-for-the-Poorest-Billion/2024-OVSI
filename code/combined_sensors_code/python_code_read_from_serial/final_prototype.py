# the pico must be running the main_combined_sensors.py micropython code
# the main_combined_sensors.py code should be calibrated using the offset_calibration.py code
# this code plots the accelerometer mean and std as well as the microphone mean
# the initial thresholds are set at a reasonable suggested level
# to set the thresholds properly set the code running and press the button on the device
# the device should be on the concentrator and the concentrator should be running
# the screen will turn orange for 10s whilst it perfoms the threshold calibration
# once the calibration is performed, the screen will show green or red
# green suggests that the device thinks the concentrator is running
# red suggests that the device thinks the concentrator is off

import serial
import matplotlib.pyplot as plt
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
acc_std_data = deque([0]*window_size, maxlen=window_size)
acc_mean_data = deque([0]*window_size, maxlen=window_size)
mic_mean_data = deque([0]*window_size, maxlen=window_size)
acc_buffer = deque([0]*1000, maxlen=1000)
mic_buffer = deque([0]*1000, maxlen=1000)

buffer = deque(maxlen=1000)  # Buffer to store incoming data

# Initial guesses for thresholds
acc_mean_threshold = 0.04
acc_std_threshold = 0.02
mic_mean_threshold = 1.5

# Flag to indicate if we are recording new threshold values
recording_thresholds = False
recording_count = 0

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
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))
line1, = ax1.plot(range(window_size), acc_std_data, label='Accelerometer Standard Deviation')
line2, = ax2.plot(range(window_size), acc_mean_data, label='Accelerometer Mean')
line3, = ax3.plot(range(window_size), mic_mean_data, label='Microphone Mean')
std_line = ax1.axhline(y=acc_std_threshold, color='r', linestyle='--', label='Accelerometer Std Dev Threshold')
mean_line = ax2.axhline(y=acc_mean_threshold, color='r', linestyle='--', label='Accelerometer Mean Threshold')
mic_line = ax3.axhline(y=mic_mean_threshold, color='r', linestyle='--', label='Microphone Mean Threshold')
ax1.legend(loc='upper left')
ax1.set_ylim(0, 0.1)  # Adjust the limits according to expected std dev range
ax2.legend(loc='upper left')
ax2.set_ylim(0, 0.2)  # Adjust the limits according to your expected mean range
ax3.legend(loc='upper left')
ax3.set_ylim(0, 2)  # Adjust the limits according to your expected mic mean range

def update(frame):
    global recording_thresholds, recording_count, acc_mean_threshold, acc_std_threshold, mic_mean_threshold
    while buffer:
        line = buffer.popleft()
        
        if line == "BUTTON_PRESSED":
            recording_thresholds = True
            recording_count = 0
            fig.patch.set_facecolor('orange')
            acc_buffer.clear()
            mic_buffer.clear()
            continue

        try:
            mag, vu_value = map(float, line.split(','))
            acc_buffer.append(mag)
            mic_buffer.append(vu_value)

            if recording_thresholds:
                recording_count += 1
                if recording_count >= 1000:
                    acc_mean_threshold = 0.9 * np.mean(acc_buffer)
                    acc_std_threshold = 0.9 * np.std(acc_buffer)
                    mic_mean_threshold = 0.9 * np.mean(mic_buffer)
                    recording_thresholds = False
                    fig.patch.set_facecolor('white')
                    # Update the threshold lines on the plot
                    std_line.set_ydata([acc_std_threshold] * window_size)
                    mean_line.set_ydata([acc_mean_threshold] * window_size)
                    mic_line.set_ydata([mic_mean_threshold] * window_size)
                    
            else:
                if len(acc_buffer) >= 1000:
                    acc_std = np.std(acc_buffer)
                    acc_mean = np.mean(acc_buffer)
                    mic_mean = np.mean(mic_buffer)

                    acc_std_data.append(acc_std)
                    acc_mean_data.append(acc_mean)
                    mic_mean_data.append(mic_mean)

                    line1.set_ydata(acc_std_data)
                    line2.set_ydata(acc_mean_data)
                    line3.set_ydata(mic_mean_data)

                    # Change background color based on condition
                    if acc_mean > acc_mean_threshold and acc_std > acc_std_threshold and mic_mean > mic_mean_threshold:
                        fig.patch.set_facecolor('green')
                    else:
                        fig.patch.set_facecolor('red')
        except ValueError:
            print("Invalid line received")

    return line1, line2, line3, std_line, mean_line, mic_line

# Use a higher interval to give the system more time to update
ani = animation.FuncAnimation(fig, update, interval=50)  # Update every 50 ms
plt.show()

# Close the serial port when done
ser.close()
