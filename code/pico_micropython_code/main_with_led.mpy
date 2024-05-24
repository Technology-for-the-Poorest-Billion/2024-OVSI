#this is micropython code for the pico
#it calclates the variance of the data of the last 1000 readings (roughly 10s)
#if the variance is above a certain threshold then the led will light up
#this was an early prototype to show how the pico could be used to monitor the oxygen concentrator signals

from machine import Pin, I2C
import utime

# I2C setup
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)

# ICM-20948 I2C address
ICM20948_ADDR = 0x68

# Register addresses from the datasheet
REG_PWR_MGMT_1 = 0x06
REG_ACCEL_XOUT_H = 0x2D

# Initialize the ICM-20948
i2c.writeto_mem(ICM20948_ADDR, REG_PWR_MGMT_1, bytearray([0x01]))

# Sensitivity for ±2g (assuming we are using ±2g)
SENSITIVITY = 16384

# Offsets measured during calibration
offset_x = 0.0  # Replace with actual offset values
offset_y = -0.02  # Replace with actual offset values
offset_z = 0.07  # Replace with actual offset values

# Buffer size
BUFFER_SIZE = 1000

# Circular buffer to store the last 1000 mag values
mag_buffer = [0] * BUFFER_SIZE
buffer_index = 0
buffer_filled = False

# Variables to keep track of the sum and sum of squares
sum_mag = 0
sum_mag_squared = 0

# Initialize GPIO 15 as an output pin for the LED
led = Pin(15, Pin.OUT)

def read_calibrated_accel():
    data = i2c.readfrom_mem(ICM20948_ADDR, REG_ACCEL_XOUT_H, 6)
    accel_x = (data[0] << 8 | data[1])
    accel_y = (data[2] << 8 | data[3])
    accel_z = (data[4] << 8 | data[5])
    
    if accel_x >= 32768:
        accel_x -= 65536
    if accel_y >= 32768:
        accel_y -= 65536
    if accel_z >= 32768:
        accel_z -= 65536

    accel_x_g = accel_x / SENSITIVITY - offset_x - 1
    accel_y_g = accel_y / SENSITIVITY - offset_y
    accel_z_g = accel_z / SENSITIVITY - offset_z
    mag = (accel_x_g ** 2 + accel_y_g ** 2 + accel_z_g ** 2) ** 0.5
    return accel_x_g, accel_y_g, accel_z_g, mag

def update_variance(new_value):
    global buffer_index, buffer_filled, sum_mag, sum_mag_squared
    
    old_value = mag_buffer[buffer_index]
    
    # Update the buffer
    mag_buffer[buffer_index] = new_value
    buffer_index = (buffer_index + 1) % BUFFER_SIZE
    if buffer_index == 0:
        buffer_filled = True

    # Update sums
    sum_mag += new_value - old_value
    sum_mag_squared += new_value**2 - old_value**2
    
    count = BUFFER_SIZE if buffer_filled else buffer_index
    mean = sum_mag / count
    variance = (sum_mag_squared / count) - (mean ** 2)
    return variance

# Desired loop interval in milliseconds
desired_interval_ms = 10

while True:
    start_time = utime.ticks_ms()
    
    accel_x_g, accel_y_g, accel_z_g, mag = read_calibrated_accel()
    print('{:.3f},{:.3f},{:.3f},{:.3f}'.format(accel_x_g, accel_y_g, accel_z_g, mag))
    
    variance = update_variance(mag)
    
    if buffer_filled:
        print('Variance: {:.6f}'.format(variance))
        if variance > 0.004:
            led.value(1)  # Turn the LED on
        else:
            led.value(0)  # Turn the LED off
    
    elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time)
    sleep_time = desired_interval_ms - elapsed_time  # Calculate remaining time to sleep
    if sleep_time > 0:
        utime.sleep_ms(sleep_time)
    else:
        # If processing took longer than desired interval, print a warning
        print("Warning: Processing is slower than the desired interval")
