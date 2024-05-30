# micropython code for the pico
# combines the individual sensor codes main_acc.py and main_mic.py
# prints the accelerometer magnitude and the microphone volume unit
# results are recorded every 10ms
# calculate the offsets from offset_calibration.py

from machine import Pin, I2C, ADC
import utime
import time

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

# Offsets measured during calibration
offset_x = 0.0  # Replace with actual offset values
offset_y = -0.033  # Replace with actual offset values
offset_z = 0.056  # Replace with actual offset values

# Setup ADC (Analog to Digital Converter) on GPIO 26 (Pin 31) for microphone
mic = ADC(Pin(26))

# Variables to find the peak-to-peak amplitude of AUD output
sample_time = 10

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

    accel_x_g = accel_x / SENSITIVITY - offset_x
    accel_y_g = accel_y / SENSITIVITY - offset_y
    accel_z_g = accel_z / SENSITIVITY - offset_z
    mag = (accel_x_g ** 2 + accel_y_g ** 2 + accel_z_g ** 2) ** 0.5
    return mag

# Function to find the Peak-to-Peak Amplitude for microphone
def find_ptp_amp():
    start_time = time.ticks_ms()  # Start of sample window
    max_amp = 0
    min_amp = 65535  # 16-bit resolution of Pico ADC

    # Find the max and min of the mic output within the 50 ms timeframe
    while time.ticks_diff(time.ticks_ms(), start_time) < sample_time:
        mic_out = mic.read_u16() >> 4  # Convert 16-bit reading to 12-bit
        if mic_out < 4096:  # prevent erroneous readings
            if mic_out > max_amp:
                max_amp = mic_out  # save only the max reading
            elif mic_out < min_amp:
                min_amp = mic_out  # save only the min reading

    ptp_amp = max_amp - min_amp  # (max amp) - (min amp) = peak-to-peak amplitude
    mic_out_volts = (ptp_amp * 3.3) / 4096  # Convert ADC into voltage

    return ptp_amp

# Volume Unit Meter function: map the PTP amplitude to a volume unit between 0 and 10.
def vu_meter(mic_amp):
    # Adjust the minimum and maximum values based on your requirements
    min_val = 50   # Adjust this value based on the minimum expected amplitude
    max_val = 3000 # Adjust this value based on the maximum expected amplitude

    # Map the mic peak-to-peak amplitude to a volume unit between 0 and 10.
    # Amplitude is used instead of voltage to give a larger (and more accurate) range for the map function.
    fill = (mic_amp - min_val) * 10 / (max_val - min_val)
    fill = max(0, min(fill, 10))  # Ensure the value is within 0-10 range

    return fill

# Main loop with combined output
while True:
    # Read accelerometer data
    mag = read_calibrated_accel()
    
    # Read microphone data
    mic_output = find_ptp_amp()
    vu_value = vu_meter(mic_output)
    
    # Print the accelerometer magnitude and microphone volume unit
    print('{:.3f},{:.2f}'.format(mag, vu_value))

