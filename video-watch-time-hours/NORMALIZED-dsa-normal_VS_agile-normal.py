import os

import matplotlib.pyplot as plt
import numpy as np

# X-axis data
x = list(range(1, 30))  # X-axis data from 1 to 29

# Total watch times
total_dsa_normal_watch_time = 2.02
total_agile_normal_watch_time = 1.78

# Data for Dataset 1
y1 = [0.6, 1.6, 1.4, 0.4, 0.5, 0.8, 0.3, 0.5, 0.0, 0.2, 0.5, 0.5, 0.0, 0.4, 0.2, 0.0, 0.1, 0.0, 0.2, 0.2, 0.0, 0.4, 0.2, 0.3, 0.3, 0.0, 2.1, 0.0, 0.0]  # Y-axis data
# Normalized y1
y1_normalized = [time / total_dsa_normal_watch_time for time in y1]

# Data for Dataset 2
y2 = [0.2, 0.0, 0.0, 0.0, 0.0, 0.3, 0.0, 0.0, 0.1, 0.2, 0.0, 0.1, 0.1, 0.3, 0.0, 0.1, 0.5, 0.0, 1.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.6, 0.0]  # Y-axis data
# Normalized y2
y2_normalized = [time / total_agile_normal_watch_time for time in y2]

# Create a figure and axis objects
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), gridspec_kw={'width_ratios': [2, 1]})  # Increase the width of the figure

# Plot Dataset 1 on ax1
ax1.plot(x, y1_normalized, marker='o', color='blue', linestyle='-', label='DSA_NG')

# Plot Dataset 2 on ax1
ax1.plot(x, y2_normalized, marker='o', color='red', linestyle='-', label='APM_NG')

# Add trend lines
z1 = np.polyfit(x, y1_normalized, 1)
p1 = np.poly1d(z1)

z2 = np.polyfit(x, y2_normalized, 1)
p2 = np.poly1d(z2)

ax1.plot(x, p1(x), linestyle='--', color='blue', label=f'Trend line (DSA_NG) slope={z1[0]:.4f}')
ax1.plot(x, p2(x), linestyle='--', color='red', label=f'Trend line (APM_NG) slope={z2[0]:.4f}')

# Add horizontal and vertical lines
for i in range(1, 30):
    ax1.axvline(x=i, color='gray', linestyle='--', linewidth=0.5)  # Vertical lines

for i in np.arange(0, 1.2, 0.2):
    ax1.axhline(y=i, color='gray', linestyle='--', linewidth=0.5)  # Horizontal lines

# Set the maximum limit of the y-axis
ax1.set_ylim(0, 1.2)

# Add labels and title to the line chart
ax1.set_xlabel('Day (from 7/3/2024 to 4/4/2024)')
ax1.set_ylabel('Average Watch Time (hours)')
ax1.set_title('Normalized watch time comparison between DSA_NG and APM_NG')
ax1.legend()  # Show legend for the datasets

# Create a table showing the data points for both datasets
table_data = [['Day', 'DSA_NG', 'APM_NG']]  # Initialize the table data with column headers
for i in range(len(x)):
    table_data.append([x[i], round(y1_normalized[i], 2), round(y2_normalized[i], 2)])  # Add data for each row

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