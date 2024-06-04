# Further considerations

In this 4 week project we made a triple threshold monitoring device for oxygen concetrators that reliably indicated if the concentrator was being currently running, when tested under a range of simulated interference conditions. In order to take it further, a list of potential considerations for Ben Moore and OVSI are given below.

### Additional functions

| Function                     | Explanation                                                                                                                                                                 |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Microphone Housing           | Create more sophisticated housing for the microphone sensor to isolate sound from the concentrator and make the device more robust to external noise.                        |
| Accelerometer Housing        | Improved housing to reduce vibration damping through the attachment method. Also test to find the optimum location for the accelerometer on the concentrator casing to receive vibrations. |
| Degradation Monitoring       | Use machine learning algorithms to adjust thresholds over time as the output changes due to degradation. A very large data set would be required to allow this to be extended to include predictive maintenance. |
| Non-Orientation Specific     | Use the inbuilt gyros to eliminate the gravity component so orientation of the accelerometer is not important. This is preferable to manually zeroing the readings when there is no noise present.               |
| Visual Indicator             | Incorporating an LED on the device to give visual reading on the device will allow for immediate recognition of device failure or malfunction.                               |
| Specialised Microcontroller  | Design a microcontroller to perform the specific required function. This makes the device cheaper and smaller when mass produced.                                          |
| Fourier Analysis of Vibrations | Determine frequencies of vibrations through a Fourier analysis. This could give unique signatures for concentrators and then be used to detect degradation.                   |
| GPS tracking                 | Additional GPS tracker in device will provide additional useful information for Ministries of Health, as well as providing an extra threshold for the monitoring device to prevent transportation from being confused with use. |
| Data handling and storage                 | Determine how much of the processing will be done on the device, and how it will store any data which then needs to be transferred. |

### Additional contextual testing

| Test                    | Explanation                                                                                                                           |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Hospital Test           | There may be interferences that we have not anticipated, so testing the device in a similar environment will be useful.                             |
| Environmental conditions| Test for high heat and humidity to see impact on function of concentrator and device respectively.                                     |
| Context                 | Usability study with doctors to find the level of interaction with the device they are willing to have.                                |
