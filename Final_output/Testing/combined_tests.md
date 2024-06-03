# Combined Sensor Testing

Once the testing of the individual sensors had been completed as shown in `accelerometer_tests.md` and `microphone_tests.md`, we combined the sensors to create one complete circuit as shown in `hardware_and_circuitry.md`.

We then performed further testing to see how we could use the sensors to determine whether or not the concentrator was running. The three pieces information that were being calculated were:
- The 10s rolling mean of the accelerometer magnitude
- The 10s rolling standard deviation of the accelerometer magnitude
- The 10s rolling mean of the microphone reading

The accelerometer magnitude was being measured in "g" and the microphone output was being measured as a % of the maximum value it was capable of reading.

We then performed the following tests and plotted every rolling data point on a 3d space as shown in Figure 1:
- Concentrator off and no noise
- Concentrator on
- Concentrator off and being rolled around
- Concentrator off and being carried
- Concentrator off and noise from walking, talking and other randon Dyson Centre workshop noise

<img src="assets/3d_plot_combined_tests.png" alt="3d space of sensor output" width="800"/>

**Figure 1:** 3D scatter plot showing the datapoints from the various test scenarios.
