# Interim Presentation

### Work have we achieved to date

- Background reading of other similar applications of non-intrusive load monitoring. 
- Settled on our most promising idea for achieving operation monitoring using vibrations.
- Connected accelerometer to microcontroller.
- Written code to read and manipulate accelerometer data.
- Connected LED circuit to give visual reading. 
- 3D printed mounting solution for breadboard. 
- Tested vibrations under variety of external factors to influence threshold and measurement approach.
- Data analysis of vibration readings.
- Updated code to give accurate readings in presence of external factors.

### Setup and Testing

- The first step was to be able to read the outputs from the accelerometer. This was done using an early version of the code main_interim_prototype.mpy and we were able to read the outputs using Thonny. It returned values of the x, y and z components of the acceleration as well as the magnitude.
- In order to plot and visualise the code we used python in VS Code to read the serial output and create a live plot using the Matplotlib animate function. An example of this plot can be seen in Figure 1 below.

<img src="assets/plotter_with_magnitude.png" alt="Screenshot of python plotter" width="800"/>

**Figure 1:** Screenshot of the python script plotting the x, y, z components from the accelerometer as well as the magnitude (measured in 'g'). Shows the last 200 readings (ie 2 seconds).  

- Next we aimed to remove the gravitational component of the reading on the accelerometer, by using the inbuilt gyros. We tried various filters and algorithms but were unable to find a simple enough solution, and so to avoid wasting time we decided simply to assume the sensor always remains vertical, and remove a value of 1g from the z output.



### INCLUDE HERE A DESCRIPTION OF THE BELOW TESTS SO THAT THE CHARTS MAKE SENSE

<img src="assets/black_tests.png" alt="bar chart of tests on black concentrator" width="800"/>

**Figure 2:** Bar chart from the testing performed on the black concentrator.  


<img src="assets/blue_tests.png" alt="bar chart of tests on blue concentrator" width="800"/>

**Figure 3:** Bar chart from the testing performed on the blue concentrator.  


<img src="assets/blue_and_black_comparison.png" alt="bar chart comparing tests on black and blue concentrator" width="800"/>

**Figure 4:** Bar chart comparing the results from the black and blue concentrators.  


### Prototype

<img src="assets/interim_prototype_on.png" alt="screenshot of prototype with blue conc on" width="800"/>

**Figure 5:** Protoype output when the blue concentrator is turned on.  


<img src="assets/interim_prototype_noise_from_concentrator.png" alt="screenshot of prototype with black on next to blue" width="800"/>

**Figure 6:** Protoype output when the blue concentrator is turned off, and the black concentrator is turned on and touching.  


<img src="assets/interim_prototype_knocked.png" alt="screenshot of prototype with knock" width="800"/>

**Figure 7:** Protoype output when the blue concentrator is turned off and knocked.  


<img src="assets/interim_prototype_tilted.png" alt="screenshot of prototype with blue on tilt" width="800"/>

**Figure 8:** Protoype output when the blue concentrator is turned off and left on an uneven surface.  




https://github.com/Technology-for-the-Poorest-Billion/2024-OVSI/assets/98593139/cfc9f4a7-5daf-4990-bf7b-f4c7b06e2e5d

### Issues and steps to overcome

- First microphone gave poor data and so we reshuffled schedule to focus on vibration monitoring until a new sensor was delivered 3 days later. 
- [Alex write about code issues and how they were resolved]
- During testing we found that uneven surfaces gave accelerometer magnitude readings in similar range to when it is in operation. We also found that we got a large spike in our baseline off test that pushed the standard deviation close to the operational level. Becasue of these two things we settled on using a double threshold of magnitude and standard deviation to eliminate false readings. 

### Personal and technical development

Harry: 

- Learned about the climate we are implementing our solution into. 
- Learned how to connect different sensors to a variety of microcontrollers and how to wire an LED circuit. Self taught from online manuals.
- Learned how to solder connections with help from a technician in the dyson centre.
- Learned how to use the 3D printer to make the clips. 

Alex:

- coding

### Updated project development timeline 

- Week 1: Understanding the problem and identifying potential solutions.
- Week 2: Setup of vibration monitoring prototype and successful testing. 
- Week 3: Sound monitoring feasability test, refinement of vibration prototype. 
- Week 4: Documenting our invisiged next steps for the company. Project deliverables.

Slight reshuffle due to a delay in sound sensor arriving but overall ahead of schedule.

### Plan for project completion 

- 2 days max testing microphone as it will likely be highly innacurate but worth ruling out with concrete testing. 
- Further analysis of test data for vibrations to set design threshold. 
- Run longer timeframe test to establish accuracy.
- Decide if degredation monitoring is feasible. Create a document of next actions and key feedback for Ben.
