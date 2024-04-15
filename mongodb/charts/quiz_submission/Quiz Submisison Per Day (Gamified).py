import os
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Sample data
ranges = [
    {"x": "07-Mar-2024", "y_series_0": -20, "y": 20},
    {"x": "08-Mar-2024", "y_series_0": 915, "y": 1170},
    {"x": "09-Mar-2024", "y_series_0": 1190, "y": 1530},
    {"x": "10-Mar-2024", "y_series_0": 1655, "y": 2140},
    {"x": "11-Mar-2024", "y_series_0": 1225, "y": 1910},
    {"x": "12-Mar-2024", "y_series_0": 1585, "y": 2310},
    {"x": "13-Mar-2024", "y_series_0": 915, "y": 1470},
    {"x": "14-Mar-2024", "y_series_0": 960, "y": 1710},
    {"x": "15-Mar-2024", "y_series_0": 1460, "y": 1880},
    {"x": "16-Mar-2024", "y_series_0": 1325, "y": 2270},
    {"x": "17-Mar-2024", "y_series_0": 1755, "y": 4720},
    {"x": "18-Mar-2024", "y_series_0": 3410, "y": 8090},
    {"x": "19-Mar-2024", "y_series_0": 615, "y": 920},
    {"x": "20-Mar-2024", "y_series_0": 505, "y": 860},
    {"x": "21-Mar-2024", "y_series_0": 425, "y": 990},
    {"x": "22-Mar-2024", "y_series_0": 410, "y": 570},
    {"x": "23-Mar-2024", "y_series_0": 180, "y": 840},
    {"x": "24-Mar-2024", "y_series_0": 205, "y": 460},
    {"x": "25-Mar-2024", "y_series_0": 785, "y": 960},
    {"x": "26-Mar-2024", "y_series_0": 330, "y": 790},
    {"x": "27-Mar-2024", "y_series_0": 470, "y": 710},
    {"x": "28-Mar-2024", "y_series_0": 1530, "y": 1840},
    {"x": "29-Mar-2024", "y_series_0": 1175, "y": 1310},
    {"x": "30-Mar-2024", "y_series_0": 2165, "y": 2410},
    {"x": "31-Mar-2024", "y_series_0": 1290, "y": 1710},
    {"x": "01-Apr-2024", "y_series_0": 1435, "y": 2190},
    {"x": "02-Apr-2024", "y_series_0": 2105, "y": 3470},
    {"x": "03-Apr-2024", "y_series_0": 4220, "y": 6020},
    {"x": "04-Apr-2024", "y_series_0": 2815, "y": 6540}
]

# Extract x, y_series_0, and y values
x = [r['x'] for r in ranges]
y_series_0 = [r['y_series_0'] for r in ranges]
y = [r['y'] for r in ranges]

# Create subplots
fig, ax = plt.subplots(figsize=(10, 6))

# Create line chart for y_series_0 against x
line1 = ax.plot(x, y_series_0, color='green', marker='o', linestyle='-', label='Hidden Rank')

# Create line chart for y against x
line2 = ax.plot(x, y, color='blue', marker='o', linestyle='-', label='Public Rank')

# Add labels and title
ax.set_xlabel('Date', fontweight='bold')
ax.set_ylabel('Values', fontweight='bold')

# Add main title
plt.suptitle('Quiz Submission Per Day (Gamified)', fontsize=16, fontweight='bold', x=0.5)
plt.title('Hidden vs Public Rank Distribution', fontsize=12, color='gray', x=0.5)

# Rotate x-axis labels for better visibility
ax.set_xticklabels(x, rotation=90, ha='right')

# Add a legend
ax.legend()

# Add the value on top of each data point for y_series_0
for i, txt in enumerate(y_series_0):
    ax.annotate(txt, (x[i], y_series_0[i]),fontsize=8, textcoords="offset points", xytext=(0, 10), ha='center')

# Add the value on top of each data point for y
for i, txt in enumerate(y):
    ax.annotate(txt, (x[i], y[i]), fontsize=8, textcoords="offset points", xytext=(0, 10), ha='center')

# Set y-axis limit to ensure all data points are visible
max_y = max(y)
ax.set_ylim(0, math.ceil(max_y / 1000) * 1000)

# Adjust layout
plt.tight_layout()

# Get the filename of the Python script
script_filename = os.path.splitext(os.path.basename(__file__))[0]

# Save the figure as a JPG with the same name as the Python script
plt.savefig(f'{script_filename}.jpg', dpi=1000)  # Set the resolution (dpi) as needed

# Show the plot
# plt.show()
