## Initial Testing:
10s moving st.dev and 10s moving average both x36 greater when black concentrator is on compared to off.
- 10s moving average becomes sensitive to the orientation of the device
- 10s moving stdev is very sensitive to small one off knocks
- perhaps a double threshold is the optimal way to do it
- If we want the device to be able to run thresholds for magnitude and standard deviation on a 10s rolling average we will need a more powerful processor.

import machine
import utime

# Initialize GPIO 15 as an output pin
led = machine.Pin(15, machine.Pin.OUT)

# Blink the LED in an infinite loop
while True:
    led.value(1)  # Turn the LED on
    utime.sleep(1)  # Wait for 1 second
    led.value(0)  # Turn the LED off
    utime.sleep(1)



# Microphone testing

import machine
import utime

# Initialize ADC on GPIO 26 (ADC0)
adc = machine.ADC(26)

while True:
    # Read analog value from the sensor
    sound_level = adc.read_u16()  # Reads a 16-bit value (0-65535)
    
    # Print the sound level
    print("Sound Level:", sound_level)
    
    # Wait for a short period before reading again
    utime.sleep(0.1)