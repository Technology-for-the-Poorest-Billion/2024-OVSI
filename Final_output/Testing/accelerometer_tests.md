# Accelerometer Testing

In order to test the robustness of the accelerometer sensor we recorded the accelerometer output over a range of different tests:
- measuring the output when the sensor is on a concentrator and the concentrator is running.
- measuring the output when the sensor is on a concentrator and the concentrator is turned off.
- measuring the output when the concentrator is turned off but another concentrator is running and making direct contact.
- measuring the output when the concentrator is turned off but another concentrator is running 10cm away.
- measuring the output when the concentrator is turned off but there is external noise from walking, talking, rolling a trolley and other noises from the Dyson Centre workshop.
- measuring the output when the concentrator is turned off but it has been left on an uneven slope.

Each of these tests were performed firstly with the accelerometer on the black oxygen concentrator, and using the blue concentrator to make noise in the other tests. Then they were performed with the accelerometer on the blue concentrator and the black concentrator was used to make noise.

In order to present the results, a 1000 reading (i.e. roughly 10 seconds) rolling mean and standard deviation were recorded throughout the duration of the 120 second test. In order to assess how well these measures can determine whether or not the concentrator is turned on or off, the charts below show the smallest readings of mean and standard deviation for the concentrator on case, and then the largest readings of mean and standard deviation for the other noisy test cases.

<img src="assets/Black_tests.png" alt="bar chart of black oc tests" width="800"/>

**Figure 1:** Bar chart from the testing performed on the black concentrator.  

<img src="assets/Blue_tests.png" alt="bar chart of blue oc tests" width="800"/>

**Figure 2:** Bar chart from the testing performed on the blue concentrator.  

<img src="assets/Blue_and_black_comparison.png" alt="comparison of blue and black tests" width="800"/>

**Figure 3:** Bar chart comparing the data between the black and blue concentrator tests.