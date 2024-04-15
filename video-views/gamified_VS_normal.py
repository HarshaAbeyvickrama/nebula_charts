import os

import matplotlib.pyplot as plt

# X-axis data
x = list(range(1, 30))  # X-axis data from 1 to 29

# Data for Dataset 1
y1 = [39, 131, 155, 145, 139, 89, 133, 123, 123, 274, 329, 335, 43, 82, 68, 52, 45, 38, 53, 45, 44, 62, 96, 106, 95, 97, 233, 190, 323]  # Y-axis data

# Data for Dataset 2
y2 = [16, 30, 37, 12, 12, 17, 9, 11, 2, 6, 7, 11, 6, 9, 4, 2, 9, 0, 22, 4, 0, 5, 5, 5, 5, 0, 38, 25, 0]  # Y-axis data

# Create a figure and axis objects
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), gridspec_kw={'width_ratios': [2, 1]})  # Increase the width of the figure

# Plot Dataset 1 on ax1
ax1.plot(x, y1, marker='o', color='blue', linestyle='-', label='Gamified')

# Plot Dataset 2 on ax1
ax1.plot(x, y2, marker='o', color='red', linestyle='-', label='Non-gamified')

# Add horizontal and vertical lines
for i in range(1, 30):
    ax1.axvline(x=i, color='gray', linestyle='--', linewidth=0.5)  # Vertical lines

for i in range(0, 350, 50):
    ax1.axhline(y=i, color='gray', linestyle='--', linewidth=0.5)  # Horizontal lines

# Add labels and title to the line chart
ax1.set_xlabel('Day (from 7/3/2024 to 4/4/2024)')
ax1.set_ylabel('Views')
ax1.set_title('Views comparison between gamified courses and non-gamified courses')
ax1.legend()  # Show legend for the datasets

# Create a table showing the data points for both datasets
table_data = [['Day', 'Gamified', 'Non-gamified']]  # Initialize the table data with column headers
for i in range(len(x)):
    table_data.append([x[i], y1[i], y2[i]])  # Add data for each row

# Create a table for the combined data
ax2.axis('off')  # Hide axis for the table
ax2.table(cellText=table_data, loc='center', cellLoc='center')  # Display the combined table with centered cell content

# Adjust layout to cut out the space between the line chart and table
plt.subplots_adjust(wspace=0.1)

# Get the filename of the Python script
script_filename = os.path.splitext(os.path.basename(__file__))[0]

# Save the figure as a JPG with the same name as the Python script
plt.savefig(f'{script_filename}.jpg', dpi=1000)  # Set the resolution (dpi) as needed

# Display the chart and table
plt.show()
