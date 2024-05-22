Initial Testing:
10s moving st.dev and 10s moving average both x36 greater when black concentrator is on compared to off

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