# this code is to be run on the pico
# it takes the microphone output and converts it into a volume on a scale from 0-10
# readings are taken every 50ms

from machine import ADC, Pin
import time

# Setup ADC (Analog to Digital Converter) on GPIO 26 (Pin 31)
mic = ADC(Pin(26))

# Variables to find the peak-to-peak amplitude of AUD output
sample_time = 50

# Function to find the Peak-to-Peak Amplitude
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

    # Return the PTP amplitude to use in the soundLevel function.
    # You can also return the mic_out_volts if you prefer to use the voltage level.
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

    # Print the volume unit value up to two decimal places
    print(f"{fill:.2f}")

# Main loop
while True:
    mic_output = find_ptp_amp()
    vu_meter(mic_output)
