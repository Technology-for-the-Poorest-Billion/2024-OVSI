# this code performs the functions described in the interim report
# it calculates the rolling values of mean and sd
# and then lights up an LED depending on whether they both reach the desired threshold
# this code is run standalone and does not require python on the laptop
# ensure that the led is attached to the correct pin to match the code
# code to calibrate and remove offsets in combined_sensor_code\pico_micropython_code folder

from machine import Pin, I2C  # used to interact with the pico
import utime

# I2C setup
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)  # initializes the I2C bus on bus 1, with the clock on pin 3 and data on pin 2

# ICM-20948 I2C address
ICM20948_ADDR = 0x68

# Register addresses from the datasheet for power management and accelerometer data
REG_PWR_MGMT_1 = 0x06
REG_ACCEL_XOUT_H = 0x2D

# Initialize the ICM-20948 by writing to the power management register
i2c.writeto_mem(ICM20948_ADDR, REG_PWR_MGMT_1, bytearray([0x01]))

# Sensitivity for ±2g (assuming we are using ±2g, this can be adjusted)
SENSITIVITY = 16384

# Offsets measured during calibration
offset_x = 0.0  # Replace with actual offset values
offset_y = -0.02  # Replace with actual offset values
offset_z = 0.07  # Replace with actual offset values

# Buffer size
BUFFER_SIZE = 1000  # Size of the circular buffer

# Circular buffer to store the last 1000 magnitude values
mag_buffer = [0] * BUFFER_SIZE
buffer_index = 0
buffer_filled = False

# Variables to keep track of the sum and sum of squares of magnitudes
sum_mag = 0
sum_mag_squared = 0

# Initialize GPIO 15 as an output pin for the LED
led = Pin(15, Pin.OUT)

def read_calibrated_accel():
    # Reads the current accelerometer output
    data = i2c.readfrom_mem(ICM20948_ADDR, REG_ACCEL_XOUT_H, 6)
    
    # Combines the high and low bytes to form a 16-bit output
    accel_x = (data[0] << 8 | data[1])
    accel_y = (data[2] << 8 | data[3])
    accel_z = (data[4] << 8 | data[5])
    
    # Adjusts for the two's complement representation
    if accel_x >= 32768:
        accel_x -= 65536
    if accel_y >= 32768:
        accel_y -= 65536
    if accel_z >= 32768:
        accel_z -= 65536

    # Convert raw values to g-forces and apply offsets
    accel_x_g = accel_x / SENSITIVITY - offset_x - 1
    accel_y_g = accel_y / SENSITIVITY - offset_y
    accel_z_g = accel_z / SENSITIVITY - offset_z
    mag = (accel_x_g ** 2 + accel_y_g ** 2 + accel_z_g ** 2) ** 0.5
    return accel_x_g, accel_y_g, accel_z_g, mag

def update_stats(new_value):
    # Update statistics for the circular buffer of magnitudes
    global buffer_index, buffer_filled, sum_mag, sum_mag_squared
    
    old_value = mag_buffer[buffer_index]
    
    # Update the buffer with the new value
    mag_buffer[buffer_index] = new_value
    buffer_index = (buffer_index + 1) % BUFFER_SIZE
    if buffer_index == 0:
        buffer_filled = True

    # Update sums
    sum_mag += new_value - old_value
    sum_mag_squared += new_value ** 2 - old_value ** 2
    
    count = BUFFER_SIZE if buffer_filled else buffer_index
    mean = sum_mag / count
    standard_dev = ((sum_mag_squared / count) - (mean ** 2)) ** 0.5
    return mean, standard_dev

# Desired loop interval in milliseconds
desired_interval_ms = 10

# Main loop to read accelerometer data and update statistics
while True:
    start_time = utime.ticks_ms()
    
    accel_x_g, accel_y_g, accel_z_g, mag = read_calibrated_accel()
    print('{:.3f},{:.3f},{:.3f},{:.3f}'.format(accel_x_g, accel_y_g, accel_z_g, mag))
    
    mean, standard_dev = update_stats(mag)
    
    if buffer_filled:
        print('Mean: {:.6f}, SD: {:.6f}'.format(mean, standard_dev))
        if mean > 0.04 and standard_dev > 0.02:
            led.value(1)  # Turn the LED on
        else:
            led.value(0)  # Turn the LED off
    
    elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time)
    sleep_time = desired_interval_ms - elapsed_time  # Calculate remaining time to sleep
    if sleep_time > 0:
        utime.sleep_ms(sleep_time)
    else:
        # If processing took longer than the desired interval, print a warning
        print("Warning: Processing is slower than the desired interval")
