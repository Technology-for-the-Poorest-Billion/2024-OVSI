# Further considerations

In this 4 week project we made a triple threshold monitoring device for oxygen concetrators that reliably indicated if the concentrator was being used in a range of simulated interference conditions. In order to take it further a list of potential considerations are given below.

### Next Steps

| Accelerometer                                                                                      | Microphone                                        |
|---------------------------------------------------------------------------------------------------|---------------------------------------------------|
| Create syncing program to determine threshold for concentrator automatically.                    | Specialist housing to isolate concentrator noise. |
| Machine learning to adapt threshold over time as the concentrator degrades, need to get a big enough data set to perform machine learning. | Look at coupling it with accelerometer data to give better diagnosis of problems. |
| Improved housing for accelerometer (ensure vibration are not damped) + testing to find the optimum attachment location on concentrator. |                                                   |
| Gyro used to eliminate gravity component so orientation not important, rather than manually zeroing readings. If not possible then add in additional calibration functionality. |                                                   |
| Better simulate hospital conditions to test accuracy.                                             |                                                   |
| How will it perform in the environmental conditions.                                              |                                                   |
| Create outsourcing of data for processing.                                                        |                                                   |
| LED on device to indicate if concentrator is on or off.                                           |                                                   |
| Create specialised microcontroller.                                                               |                                                   |
| Fourier analysis of vibration to identify frequency changes to degradation.                       |                                                   |
| GPS system to help with tracking and eliminate transport false positive.                          |                                                   |
| Usability study with doctors, find level of interaction with the device they are willing to do.   |                                                   |
