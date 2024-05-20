#returns x,y,z accelerations
#no offset adjustments or accounting for gravity

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

# Sensitivity for ±2g
SENSITIVITY = 16384

def read_sensor():
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

    # Convert to units of 'g' by dividing by sensitivity
    accel_x_g = accel_x / SENSITIVITY
    accel_y_g = accel_y / SENSITIVITY
    accel_z_g = accel_z / SENSITIVITY

    return accel_x_g, accel_y_g, accel_z_g

while True:
    accel_x_g, accel_y_g, accel_z_g = read_sensor()
    print('{:.2f},{:.2f},{:.2f}'.format(accel_x_g, accel_y_g, accel_z_g))
    utime.sleep(0.01)
