# micropython code for the pi pico
# returns x, y, z components and magnitude
# has offest adjustment capability
# adjusted to account for gravity by assuming sensor is placed vertically
# tries to ensure that the data is recorded as close to every 0.01s as possible
# this code is for the ICM-20948 accelerometer sensor

from machine import Pin, I2C # used to interact with the pico
import utime

# I2C setup
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000) # initialises the I2C bus on bus 1, with the clock on pin 3 and data on pin 2

# ICM-20948 I2C address
ICM20948_ADDR = 0x68

# Register addresses from the datasheet for power management and accelerometer data
REG_PWR_MGMT_1 = 0x06
REG_ACCEL_XOUT_H = 0x2D

# Initialize the ICM-20948
i2c.writeto_mem(ICM20948_ADDR, REG_PWR_MGMT_1, bytearray([0x01]))

# Sensitivity for ±2g (assuming we are using ±2g, this can be adjusted)
SENSITIVITY = 16384

# Offsets measured during calibration
offset_x = 0.0  # Replace with actual offset values
offset_y = -0.02  # Replace with actual offset values
offset_z = 0.07  # Replace with actual offset values

def read_calibrated_accel():
    # reads the current accelerometer output
    data = i2c.readfrom_mem(ICM20948_ADDR, REG_ACCEL_XOUT_H, 6)

    # combines the high and low bytes to form a 16-bit output
    accel_x = (data[0] << 8 | data[1]) 
    accel_y = (data[2] << 8 | data[3])
    accel_z = (data[4] << 8 | data[5])

    # adjusts for the twos complement representation
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

# desired loop interval in milliseconds
desired_interval_ms = 10

# this loop prints the accelerometer data
# it aims to ensure that readings are made every 0.01s

while True:
    start_time = utime.ticks_ms()
    
    accel_x_g, accel_y_g, accel_z_g, mag = read_calibrated_accel()
    print('{:.3f},{:.3f},{:.3f},{:.3f}'.format(accel_x_g, accel_y_g, accel_z_g, mag))
    
    elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time)
    sleep_time = desired_interval_ms - elapsed_time  # Calculate remaining time to sleep
    if sleep_time > 0:
        utime.sleep_ms(sleep_time)
    else:
        # If the above loop takes longer than 10 ms to run then 
        print("Warning: Processing is slower than the desired interval")
