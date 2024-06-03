### Circuitry

Final prototype breadboard setup. 

# List of components

- Breadboard
- Rasberry pi pico wh
- ICM20948 9DoF Motion Sensor Breakout
- SparkFun Analog MEMS Microphone Breakout - SPH8878LR5H-1
- 10 kΩ resistor
- Jumper wires X 10
- 6mm button

# Connections

 - **2-5V** on accelerometer to **3V3(OUT)** on pico.
 - **SDA** on accelerometer to **I2C1 SDA (GP2)** on pico.
 - **SCL** on accelerometer to **I2C1 SCL (GP3)** on pico.
 - **GND** on accelerometer to **GND** on pico.

 - **VCC** on Microphone to **3V3(OUT)** on pico.
 - **GND** on Microphone to **GND** on pico.
 - **AUD** on Microphone to **I2C1 SDA (GP26)** on pico.

 - **One leg** on Switch to **(GP15)** on pico.
 - **Opposite leg** on Switch to **GND** on pico.
 - Resistor connects **GP15** to **live rail** 

Where a pin number is specified in brackets it is required to be compatible with existing code but any GPIO pin will suffice.

For testing of each sensor seperately as the same pin connections were used.

Rasberry pi pico wh datasheet:

https://datasheets.raspberrypi.com/picow/pico-w-datasheet.pdf (03/06/2024)

# Circuit setup schematic

<img src="Assets/circuit_diagram.png" alt="Circuit diagram" width="800"/>

### Mounting solution

In order to run tests reproducably and be able to quickly mount and dismount the breadboard for alteration, we designed custom clips. These were 3D printed from PLA filiment after solidworks modelling. The STL file for the [clip](/Final_output/Hardware_and_circuitry/Assets/clip.STL) is shown in the Assets folder. Two clips were used per concentrator, superglued to a flat surface of the plastic casing. See [further considerations](/Final_output/Further_considerations/) for how this can be improved.

### Sound isolation for microphone sensor


### Concentrator testing
