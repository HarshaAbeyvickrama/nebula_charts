import os

import matplotlib.pyplot as plt

# Sample data
x = list(range(1, 30))  # X-axis data from 1 to 29
y = [5, 6, 5, 4, 4, 6, 3, 4, 1, 1, 3, 3, 2, 2, 2, 0, 2, 0, 2, 1, 0, 1, 1, 2, 1, 0, 4, 1, 0]  # Y-axis data

# Create a figure and axis objects
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), gridspec_kw={'width_ratios': [4, 1]})  # Increase the width of the figure

# Plot the line chart with markers
ax1.plot(x, y, marker='o', color='blue', linestyle='-')

# Add horizontal and vertical lines
for i in range(1, 30):
    ax1.axvline(x=i, color='gray', linestyle='--', linewidth=0.5)  # Vertical lines

for i in range(0, 10, 2):
    ax1.axhline(y=i, color='gray', linestyle='--', linewidth=0.5)  # Horizontal lines

# Set the maximum limit of the y-axis to 30.0
ax1.set_ylim(0, 10)

# Add labels and title to the line chart
ax1.set_xlabel('Day (from 7/3/2024 to 4/4/2024)')
ax1.set_ylabel('Returning Viewers')
ax1.set_title('Returning viewers for DSA_NG')

# Create a table showing the data points
table_data = [[x[i], y[i]] for i in range(len(x))]  # Convert data into a table format
ax2.axis('off')  # Hide axis for the table
ax2.table(cellText=table_data, colLabels=['Day', 'Views'], loc='center', colWidths=[0.3, 0.3])  # Adjust column widths

# Adjust layout to cut out the space between the line chart and table
plt.subplots_adjust(wspace=0)

# Get the filename of the Python script
script_filename = os.path.splitext(os.path.basename(__file__))[0]

# Save the figure as a JPG with the same name as the Python script
plt.savefig(f'{script_filename}.jpg', dpi=1000)  # Set the resolution (dpi) as needed

# Display the chart and table
plt.show()
