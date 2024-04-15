import os
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Sample data
ranges = [
    {"x": "07-Mar-2024", "y": 1},
    {"x": "08-Mar-2024", "y": 7},
    {"x": "09-Mar-2024", "y": 13},
    {"x": "10-Mar-2024", "y": 17},
    {"x": "11-Mar-2024", "y": 17},
    {"x": "12-Mar-2024", "y": 43},
    {"x": "13-Mar-2024", "y": 12},
    {"x": "14-Mar-2024", "y": 12},
    {"x": "15-Mar-2024", "y": 34},
    {"x": "16-Mar-2024", "y": 25},
    {"x": "17-Mar-2024", "y": 48},
    {"x": "18-Mar-2024", "y": 104},
    {"x": "19-Mar-2024", "y": 10},
    {"x": "20-Mar-2024", "y": 5},
    {"x": "21-Mar-2024", "y": 11},
    {"x": "22-Mar-2024", "y": 2},
    {"x": "23-Mar-2024", "y": 8},
    {"x": "24-Mar-2024", "y": 8},
    {"x": "25-Mar-2024", "y": 18},
    {"x": "26-Mar-2024", "y": 7},
    {"x": "27-Mar-2024", "y": 11},
    {"x": "28-Mar-2024", "y": 20},
    {"x": "29-Mar-2024", "y": 16},
    {"x": "30-Mar-2024", "y": 31},
    {"x": "31-Mar-2024", "y": 32},
    {"x": "01-Apr-2024", "y": 17},
    {"x": "02-Apr-2024", "y": 22},
    {"x": "03-Apr-2024", "y": 60},
    {"x": "04-Apr-2024", "y": 114}
]

# Extract x and y values
x = [r['x'] for r in ranges]
y = [int(r['y']) for r in ranges]

# Create subplots
fig, ax = plt.subplots(figsize=(10, 6))

# Create a line chart on the first subplot
line = ax.plot(x, y, color='green', marker='o', linestyle='-')

# Add labels and title
ax.set_xlabel('Date', fontweight='bold')
ax.set_ylabel('Quiz Submissions', fontweight='bold')

# Add main title
plt.suptitle('Quiz Submission Per Day', fontsize=16, fontweight='bold', x=0.5)
plt.title('Agile Project Management - (March 08 - April 05)', fontsize=12, color='gray', x=0.5)

# Rotate x-axis labels for better visibility
ax.set_xticklabels(x, rotation=90, ha='right')

# Set y-axis limit to ensure all data points are visible
max_y = max(y)
ax.set_ylim(0, math.ceil(max_y / 20) * 20)

ax.yaxis.set_major_locator(MaxNLocator(integer=True))

# Add count as text to the data points
for i, txt in enumerate(y):
    ax.annotate(txt, (x[i], y[i]), textcoords="offset points", xytext=(0, 10), ha='center')

# Get the filename of the Python script
script_filename = os.path.splitext(os.path.basename(__file__))[0]

plt.tight_layout()
# Save the figure as a JPG with the same name as the Python script
plt.savefig(f'{script_filename}.jpg', dpi=1000)  # Set the resolution (dpi) as needed
