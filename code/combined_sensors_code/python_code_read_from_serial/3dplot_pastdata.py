# takes the data from any file saved using the export_to_excel.py code in the combined_sensors_code folder
# plots it on a 3d graph
# planes can be adjusted to show any required threshold value

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Load the data from the Excel file
file_path = './combined_sensors/3_output_carried.xlsx' # change this to the required file name and location
df = pd.read_excel(file_path)

# Extract the columns into lists
std_dev_data = df['Standard Deviation'].tolist()
avg_data = df['Mean Magnitude'].tolist()
mic_avg_data = df['Microphone Output'].tolist()

# Initialize the plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the data
sc = ax.scatter(std_dev_data, avg_data, mic_avg_data, c='b', marker='o')
ax.set_xlabel('Standard Deviation')
ax.set_ylabel('Average Magnitude')
ax.set_zlabel('Microphone Mean Magnitude')
ax.set_xlim(0, 0.1)
ax.set_ylim(0, 0.2)
ax.set_zlim(0, 2)

std_threshold = 0.02
avg_threshold = 0.04
mic_threshold = 1.4

# Define grid for threshold planes
x = np.linspace(0, 0.1, 10)
y = np.linspace(0, 0.2, 10)
z = np.linspace(0, 2, 10)

# Create meshgrid for planes
Y, Z = np.meshgrid(y, z)
X1, Z1 = np.meshgrid(x, z)
X2, Y2 = np.meshgrid(x, y)

# Plot threshold planes
ax.plot_surface(np.full_like(Y, std_threshold), Y, Z, alpha=0.3, color='r')  # Plane at x = 0.02
ax.plot_surface(X1, np.full_like(X1, avg_threshold), Z1, alpha=0.3, color='g')  # Plane at y = 0.04
ax.plot_surface(X2, Y2, np.full_like(X2, mic_threshold), alpha=0.3, color='b')  # Plane at z = 1.4

plt.show()
