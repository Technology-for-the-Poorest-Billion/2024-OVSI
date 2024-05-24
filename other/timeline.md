### AB 16/05/24
- Acquired 4 Nucleo-144 F746ZG microcontrollers
- Did full chip erase and updated firmware to ensure they would run properly
- Judged the use of VS Code and PlatformIO as the best way to program the microcontrollers using open source software
- Did some basic programming using the LED lights to ensure I could sync the microcontroller and my laptop
- Used preprocessor directives to conditionally compile code based on using unique identifiers for each board
- Used the serial monitor to print a continuous output based off button presses
- Ordered one accelerometer, one microphone and an electronics kit with a breadboard

### HA 17/05/24
- Researched use cases of non intrusive load monitoring with accelerometers.
- Assessed feasability for use on an oxygen concentrator.
- Made a list of necessary hardware and did a cost estimation per unit.
- Made an account of software required to process raw vibration data.
- Found modifications required for acoustic sensor.
- Brief familiarisation with sensors and microctrollers we have / have on order. 

### AB 20/05/24
- Attempted set up of Arduino Uno without success
- Ben supplied us with breadboard, sensors and a raspberry pi pico wh
- Attached the pico and accelerometer to the breadboard
- Coded the pico to output the acceleration components
- Used python to create a live plot of the serial output
- Had to adjust the plotter code to include a buffer to remove the significant delay
- Tried multiple ways to remove the gravitational component of acceleration without success
- Eventually agreed to leave sensor vertical and reduce the x component by 1g
- Wrote code to save the serial output as a .csv file
- Took multiple recordings of different scenarios to be analysed in the coming days

### HA 20/05/24
Joint with Alex:

'- Ben supplied us with breadboard, sensors and a raspberry pi pico wh
- Attached the pico and accelerometer to the breadboard
- Eventually agreed to leave sensor vertical and reduce the x component by 1g'
  
- Picked up new concentrator from Ben.
- Researched sensitivity of accelerometer and likely primary and background signals.
- Did some troubleshooting of code with Alex although largely left him to write it.
- Soldered accelerometer connections.
- Created CAD model for clips.
- Refined CAD model after intial 3D print.
- Printed clips for attachment of breadboard to casing of concentrator.

  
