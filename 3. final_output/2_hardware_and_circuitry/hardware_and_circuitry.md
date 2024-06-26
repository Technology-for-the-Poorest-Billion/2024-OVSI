# Circuitry for Final Breadboard Layout

### List of components

- Breadboard
- Raspberry Pi Pico WH
- ICM20948 9DoF Motion Sensor Breakout
- SparkFun Analog MEMS Microphone Breakout - SPH8878LR5H-1
- 10 kΩ resistor
- Jumper wires X 10
- 6mm button
- Header pins

### Connections

Initially the header pins were soldered to the accelerometer and microphone sensors to allow connections to the Pi Pico. The connections between the Pi Pico and the sensors are as follows:

 - **2-5V** on accelerometer to **3V3(OUT)** on pico
 - **SDA** on accelerometer to **I2C1 SDA (GP2)** on pico
 - **SCL** on accelerometer to **I2C1 SCL (GP3)** on pico
 - **GND** on accelerometer to **GND** on pico

 - **VCC** on microphone to **3V3(OUT)** on pico
 - **GND** on microphone to **GND** on pico
 - **AUD** on microphone to **I2C1 SDA (GP26)** on pico

 - **One leg** of the switch to **(GP15)** on pico
 - **Opposite leg** of the switch to **GND** on pico
 - A 10 kΩ resistor connects **GP15** to **live rail** 

Where a pin number is specified in brackets it is required to be compatible with existing code but any GPIO pin will suffice.

Where testing of each sensor separately has been performed, the same pin connections were used.

Raspberry Pi Pico WH datasheet:

https://datasheets.raspberrypi.com/picow/pico-w-datasheet.pdf , Accessed: (03/06/2024)

### Circuit setup schematic

<img src="Assets/circuit_diagram.png" alt="Circuit diagram" width="800"/>

The microphone is shown attached to the breadboard for the purpose of the schematic, but tests were run with it inside a separate casing but still wired to the pico with the connections as shown. The casing is shown in later sections.

# Mounting solutions

### Breadboard attachment

In order to run tests reproducibly and to be able to quickly mount and dismount the breadboard for alteration, we designed custom clips. These were 3D printed from PLA filament after SolidWorks modelling. The STL file for the [clip](</3. final_output/2_hardware_and_circuitry/Assets/clip.STL>) is shown in the Assets folder. Two clips were used per concentrator, superglued to a flat surface of the plastic casing. See [further considerations](</3. final_output/4_further_considerations/>) for how this can be improved.

### Sound isolation for microphone sensor

As seen in [testing](</3. final_output/5_testing_results/>), initial microphone tests were not promising for differentiating between concentrator sound and background noise. In order to rectify this, a solution was required to isolate the concentrator noise and exclude external noise. 
To do this as a rapid prototype, the sensor was taped to the inside of a box with a hole facing the concentrator. The box was then filled with foam to exclude external noise. The setup is shown below with the box open for aid of visualisation:

<img src="Assets/Foam_fill.png" alt="Microphone noise isolation" width="300"/>

The data for the success of this setup is shown in the `5_testing_results` section.

# Concentrator testing

### Concentrators used for testing

We were using two concentrators for testing: 

- Drive Devilbiss 10 Litre Compact Oxygen Concentrator 1025 
- Philips Respironics EverFlo 5L Oxygen Concentrator

They are both on the upper end of the price range, but the Philips concentrator well resembled the concentrators that are used in practice, both in terms of its output(5L) and its noise level (43dB). The most common concentrators that we are designing this device for are in the 40-50dB range. The Devilbiss concentrator is reported at 69dB operational noise level. This made it a useful worst-case scenario for many of our interference tests, where we would monitor the quiet concentrator with the loud one running nearby. 

### Final Setup 

<img src="Assets/Blue.jpeg" alt="Final setup on EverFlo" width="500"/>

The micro usb is connected to a laptop which uses Thonny to code the Raspberry Pi Pico WH, and Python to read the accelerometer and microphone outputs through the serial port.


