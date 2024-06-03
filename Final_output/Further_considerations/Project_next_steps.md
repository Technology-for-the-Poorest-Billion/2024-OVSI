# Further considerations

In this 4 week project we made a triple threshold monitoring device for oxygen concetrators that reliably indicated if the concentrator was being used in a range of simulated interference conditions. In order to take it further a list of potential considerations are given below.

### Next Steps

| Function                     | Explanation                                                                                                                                                                 |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Microphone Housing           | Create more sophisticated housing for the microphone sensor to isolate input from the concentrator and make the device more robust to external noise.                        |
| Accelerometer Housing        | Improved housing to reduce vibration damping through the attachment method. Also test to find the optimum location for the accelerometer on the concentrator casing to receive vibrations. |
| Degradation Monitoring       | Use machine learning algorithms to adjust thresholds over time as function fluctuates due to degradation. A very large data set would be required to allow this to be extended to predictive maintenance. |
| Non-Orientation Specific     | Use gyro to eliminate the gravity component so orientation is not important. This is preferable to manually setting the readings to zero for the still case.               |
| Visual Indicator             | Incorporating an LED on the device to give visual reading on the device will allow for immediate recognition of device failure or malfunction.                               |
| Specialised Microcontroller  | Design a microcontroller to perform the specific required function. This makes the device cheaper and smaller when mass produced.                                          |
| Fourier Analysis of Vibrations | Determine frequencies of vibrations through a Fourier analysis. This could give unique signatures for concentrators and be used to detect degradation.                   |
| GPS tracking                 | Additional GPS tracker in device will provide additional useful information as well as providing an extra threshold for use monitoring to prevent transportation from being confused with use. |
