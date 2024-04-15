import os

import matplotlib.pyplot as plt
import numpy as np

# X-axis data
x = list(range(1, 30))  # X-axis data from 1 to 29

# Total videos
total_dsa_gamified_videos = 52
total_agile_gamified_videos = 41

# Data for Dataset 1
y1 = [30, 89, 113, 95, 83, 35, 93, 78, 71, 203, 239, 206, 25, 67, 39, 40, 33, 22, 34, 23, 26, 55, 43, 50, 50, 78, 180, 165, 181]  # Y-axis data
# Normalized y1
y1_normalized = [view_count / total_dsa_gamified_videos for view_count in y1]

# Data for Dataset 2
y2 = [9, 42, 42, 50, 56, 54, 40, 45, 52, 71, 90, 129, 18, 15, 29, 12, 12, 16, 19, 22, 18, 7, 53, 56, 45, 19, 53, 25, 142]  # Y-axis data
# Normalized y1
y2_normalized = [view_count / total_agile_gamified_videos for view_count in y2]

# Create a figure and axis objects
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), gridspec_kw={'width_ratios': [2, 1]})  # Increase the width of the figure

# Plot Dataset 1 on ax1
ax1.plot(x, y1_normalized, marker='o', color='blue', linestyle='-', label='DSA_G')

# Plot Dataset 2 on ax1
ax1.plot(x, y2_normalized, marker='o', color='red', linestyle='-', label='APM_G')

# Add trend lines
z1 = np.polyfit(x, y1_normalized, 1)
z2 = np.polyfit(x, y2_normalized, 1)
p1 = np.poly1d(z1)
p2 = np.poly1d(z2)

# Plot Dataset 1 with trend line
ax1.plot(x, p1(x), linestyle='--', color='blue', label=f'DSA_G Trend (slope={z1[0]:.4f})')

# Plot Dataset 2 with trend line
ax1.plot(x, p2(x), linestyle='--', color='red', label=f'APM_G Trend (slope={z2[0]:.4f})')

# Add horizontal and vertical lines
for i in range(1, 30):
    ax1.axvline(x=i, color='gray', linestyle='--', linewidth=0.5)  # Vertical lines

for i in range(0, 5, 1):
    ax1.axhline(y=i, color='gray', linestyle='--', linewidth=0.5)  # Horizontal lines

# Set the maximum limit of the y-axis to 30.0
ax1.set_ylim(0, 5.0)

# Add labels and title to the line chart
ax1.set_xlabel('Day (from 7/3/2024 to 4/4/2024)')
ax1.set_ylabel('Normalized Video Views per Student')
ax1.set_title('Normalized views comparison between DSA_G and APM_G')
ax1.legend()  # Show legend for the datasets

# Create a table showing the data points for both datasets
table_data = [['Day', 'DSA_G', 'APM_G']]  # Initialize the table data with column headers
for i in range(len(x)):
    table_data.append([x[i], round(y1_normalized[i], 5), round(y2_normalized[i], 5)])  # Add data for each row

# Create a table for the combined data
ax2.axis('off')  # Hide axis for the table
ax2.table(cellText=table_data, loc='center', cellLoc='center', colWidths=[0.2, 0.4, 0.4])  # Display the combined table with centered cell content

# Adjust layout to cut out the space between the line chart and table
plt.subplots_adjust(wspace=0.1)

# Get the filename of the Python script
script_filename = os.path.splitext(os.path.basename(__file__))[0]

# Save the figure as a JPG with the same name as the Python script
plt.savefig(f'{script_filename}.jpg', dpi=1000)  # Set the resolution (dpi) as needed

# Display the chart and table
plt.show()