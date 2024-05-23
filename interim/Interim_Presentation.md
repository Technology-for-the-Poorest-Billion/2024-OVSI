# Interim Presentation

### Work have we achieved to date

- Background reading of other similar applications of NILM. 
- Settled on our most promising idea for achieving operation monitoring using vibrations.
- Connected accelerometer to microcontroller.
- Written code to read and manipulate accelerometer data.
- Connected LED circuit to give visual reading. 
- 3D printed mounting solution for breadboard. 
- Tested vibrations under variety of external factors to influence threshold and measurement approach.
- Data analysis of vibration readings.
- Updated code to give accurate readings in presence of external factors.

### Prototype and testing

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

- 

### Updated project development timeline 

- Week 1: Understanding the problem and identifying potential solutions.
- Week 2: Setup of vibration monitoring prototype and successful testing. 
- Week 3: Sound monitoring feasability test, refinement of vibration prototype. 
- Week 4: Documenting our invisiged next steps for the company. Project deliverables.

Slight reshuffle due to a delay in sound sensor arriving but overall ahead of schedule.

### Plan for project completion 

- 2 days max testing microphone as it will likely be highly innacurate but worth ruling out with concrete testing. 
- Further analysis of test data for vibrations to set design threshold. 
- Finalise prototype with LED to show operation. 
- Run longer timeframe test to establish accuracy. 
