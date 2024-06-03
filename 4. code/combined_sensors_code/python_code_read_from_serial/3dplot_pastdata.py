# takes the data from any file saved using the export_to_excel.py code in the combined_sensors_code folder
# plots it on a 3d graph
# planes can be adjusted to show any required threshold value

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Load the data from the Excel file
file_path = './combined_sensors/blue_on.xlsx'
df1 = pd.read_excel(file_path)
df1['Microphone Output'] *= 10  # Increase microphone values by a factor of 10

# Extract the columns into lists
std_dev_data_1 = df1['Standard Deviation'].tolist()
avg_data_1 = df1['Mean Magnitude'].tolist()
mic_avg_data_1 = df1['Microphone Output'].tolist()

# Load the data from the Excel file
file_path = './combined_sensors/no_noise.xlsx'
df2 = pd.read_excel(file_path)
df2['Microphone Output'] *= 10  # Increase microphone values by a factor of 10

# Extract the columns into lists
std_dev_data_2 = df2['Standard Deviation'].tolist()
avg_data_2 = df2['Mean Magnitude'].tolist()
mic_avg_data_2 = df2['Microphone Output'].tolist()

# Load the data from the Excel file
file_path = './combined_sensors/rolling_concentrator.xlsx'
df3 = pd.read_excel(file_path)
df3['Microphone Output'] *= 10  # Increase microphone values by a factor of 10

# Extract the columns into lists
std_dev_data_3 = df3['Standard Deviation'].tolist()
avg_data_3 = df3['Mean Magnitude'].tolist()
mic_avg_data_3 = df3['Microphone Output'].tolist()

# Load the data from the Excel file
file_path = './combined_sensors/carrying_concentrator.xlsx'
df4 = pd.read_excel(file_path)
df4['Microphone Output'] *= 10  # Increase microphone values by a factor of 10

# Extract the columns into lists
std_dev_data_4 = df4['Standard Deviation'].tolist()
avg_data_4 = df4['Mean Magnitude'].tolist()
mic_avg_data_4 = df4['Microphone Output'].tolist()

# Load the data from the Excel file
file_path = './combined_sensors/talking_walking_disturbances_noise.xlsx'
df5 = pd.read_excel(file_path)
df5['Microphone Output'] *= 10  # Increase microphone values by a factor of 10

# Extract the columns into lists
std_dev_data_5 = df5['Standard Deviation'].tolist()
avg_data_5 = df5['Mean Magnitude'].tolist()
mic_avg_data_5 = df5['Microphone Output'].tolist()

# Initialize the plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the data
sc1 = ax.scatter(std_dev_data_1, avg_data_1, mic_avg_data_1, c='b', marker='o', label='Blue On')
sc2 = ax.scatter(std_dev_data_2, avg_data_2, mic_avg_data_2, c='g', marker='o', label='No Noise')
sc3 = ax.scatter(std_dev_data_3, avg_data_3, mic_avg_data_3, c='pink', marker='o', label='Rolling Concentrator')
sc4 = ax.scatter(std_dev_data_4, avg_data_4, mic_avg_data_4, c='r', marker='o', label='Carrying Concentrator')
sc5 = ax.scatter(std_dev_data_5, avg_data_5, mic_avg_data_5, c='y', marker='o', label='Talking Walking Disturbances')

ax.set_xlabel('Accelerometer Rolling \n Standard Deviation "g"')
ax.set_ylabel('Accelerometer Rolling Mean "g"')
ax.set_zlabel('Microphone Rolling Mean, \n % of Maximum Mic Reading')
ax.set_xlim(0, 0.15)
ax.set_ylim(0, 0.3)
ax.set_zlim(0, 30)  # Adjusted z-limit to accommodate increased values

std_threshold = 0.02
avg_threshold = 0.04
mic_threshold = 14  # Adjusted threshold for increased values

# Define grid for threshold planes
x = np.linspace(0, 0.15, 10)
y = np.linspace(0, 0.3, 10)
z = np.linspace(0, 30, 10)  # Adjusted z-range to accommodate increased values

# Create meshgrid for planes
Y, Z = np.meshgrid(y, z)
X1, Z1 = np.meshgrid(x, z)
X2, Y2 = np.meshgrid(x, y)

# Plot threshold planes
ax.plot_surface(np.full_like(Y, std_threshold), Y, Z, alpha=0.3, color='r')  # Plane at x = 0.02
ax.plot_surface(X1, np.full_like(X1, avg_threshold), Z1, alpha=0.3, color='g')  # Plane at y = 0.04
ax.plot_surface(X2, Y2, np.full_like(X2, mic_threshold), alpha=0.3, color='b')  # Plane at z = 14

# Add legend
ax.legend()

plt.show()
