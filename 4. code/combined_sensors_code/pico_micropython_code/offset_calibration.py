# reads 10s of accelerometer output to calculate the offset
# makes no assumptions about the orientation of the accelerometer
# check any other code to see if a value of 1 is being subtracted from the z component to remove the effect of gravity already
# these outputs can be put into the offset section of any pico code relating to the accelerometer

from machine import Pin, I2C
import utime

# I2C setup for accelerometer
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

    accel_x_g = accel_x / SENSITIVITY 
    accel_y_g = accel_y / SENSITIVITY
    accel_z_g = accel_z / SENSITIVITY
    return accel_x_g, accel_y_g, accel_z_g

# Number of readings to average
num_readings = 1000

# Initialize sums for averaging
sum_accel_x = 0
sum_accel_y = 0
sum_accel_z = 0

# Main loop for collecting readings
for _ in range(num_readings):
    accel_x_g, accel_y_g, accel_z_g = read_calibrated_accel()
    sum_accel_x += accel_x_g
    sum_accel_y += accel_y_g
    sum_accel_z += accel_z_g
    utime.sleep_ms(10)  # delay between readings to simulate the original sampling rate

# Calculate averages
avg_accel_x = sum_accel_x / num_readings
avg_accel_y = sum_accel_y / num_readings
avg_accel_z = sum_accel_z / num_readings

# Print the average values
print('Average Acceleration Values:')
print('X: {:.3f} g'.format(avg_accel_x))
print('Y: {:.3f} g'.format(avg_accel_y))
print('Z: {:.3f} g'.format(avg_accel_z))
