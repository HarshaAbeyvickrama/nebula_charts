import os

import matplotlib.pyplot as plt

# X-axis data
x = list(range(1, 30))  # X-axis data from 1 to 29

# Data for Dataset 1
y1 = [10, 20, 24, 29, 27, 20, 24, 21, 28, 30, 38, 32, 13, 12, 11, 13, 13, 7, 14, 14, 11, 14, 16, 17, 18, 20, 27, 23, 17]  # Y-axis data

# Data for Dataset 2
y2 = [6, 6, 6, 4, 4, 7, 3, 5, 1, 2, 3, 4, 2, 2, 2, 0, 3, 0, 2, 1, 0, 1, 1, 2, 1, 0, 4, 2, 0]  # Y-axis data

# Create a figure and axis objects
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), gridspec_kw={'width_ratios': [2, 1]})  # Increase the width of the figure

# Plot Dataset 1 on ax1
ax1.plot(x, y1, marker='o', color='blue', linestyle='-', label='Gamified')

# Plot Dataset 2 on ax1
ax1.plot(x, y2, marker='o', color='red', linestyle='-', label='Non-gamified')

# Add horizontal and vertical lines
for i in range(1, 30):
    ax1.axvline(x=i, color='gray', linestyle='--', linewidth=0.5)  # Vertical lines

for i in range(0, 50, 10):
    ax1.axhline(y=i, color='gray', linestyle='--', linewidth=0.5)  # Horizontal lines

# Set the maximum limit of the y-axis to 30.0
ax1.set_ylim(0, 50)

# Add labels and title to the line chart
ax1.set_xlabel('Day (from 7/3/2024 to 4/4/2024)')
ax1.set_ylabel('Returning Viewers')
ax1.set_title('Returning viewers comparison between gamified courses and non-gamified courses')
ax1.legend()  # Show legend for the datasets

# Create a table showing the data points for both datasets
table_data = [['Day', 'Gamified', 'Non-gamified']]  # Initialize the table data with column headers
for i in range(len(x)):
    table_data.append([x[i], y1[i], y2[i]])  # Add data for each row

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
