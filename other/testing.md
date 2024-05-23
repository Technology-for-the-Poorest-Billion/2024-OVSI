## Initial Testing:
10s moving st.dev and 10s moving average both x36 greater when black concentrator is on compared to off.

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