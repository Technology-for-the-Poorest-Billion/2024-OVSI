# Final Prototype Demonstration

Following prior testing, we had decided that our monitoring system would use a threshold based system whereby all three thresholds have to be met in order to signal that the concentrator is running. These three thresholds are related to:
- a 10 second rolling mean of the accelerometer magnitude
- a 10 second rolling standard deviation of the accelerometer magnitude
- a 10 second rolling mean of the microphone magnitude

In order to display the current status of the monitoring system in the figures below, the following colour coding is used:
- red signals that the concentrator is not running
- orange signals that the monitoring device is undergoing threshold calibration
- green signals that the concentrator is running

The below figures now run through an example test of the monitoring system.



<img src="assets/off_red.png" alt="prototype_start_up_page" width="800"/>

**Figure 1:** Screenshot of prototype when the oxygen concentrator is turned off and there is no noise.

<img src="assets/on_red.png" alt="wrongly set thresholds" width="800"/>

**Figure 2:** Screenshot of prototype when the oxygen concentrator is turned on but the thresholds have not been calibrated.

<img src="assets/on_orange.png" alt="threshold adjustment" width="800"/>

**Figure 3:** Screenshot of prototype when the oxygen concentrator is turned on and the thresholds are being calibrated.

<img src="assets/on_green.png" alt="working thresholds" width="800"/>

**Figure 4:** Screenshot of prototype when the oxygen concentrator is turned on and the thresholds have been correctly set.

<img src="assets/off_red_with_noise.png" alt="dealing with noise" width="800"/>

**Figure 5:** Screenshot of prototype when the oxygen concentrator is turned off and the thresholds have been correctly set, but the concentrator has been left on uneven ground and there is noise from another nearby concentrator.


