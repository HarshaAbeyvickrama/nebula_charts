import math
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Sample data
ranges = [
    {"x": "-400 - -350", "y": 1},
    {"x": "-300 - -250", "y": 1},
    {"x": "-150 - -100", "y": 1},
    {"x": "-50 - 0", "y": 2},
    {"x": "0 - 50", "y": 6},
    {"x": "50 - 100", "y": 5},
    {"x": "100 - 150", "y": 2},
    {"x": "150 - 200", "y": 2},
    {"x": "200 - 250", "y": 1},
    {"x": "250 - 300", "y": 4},
    {"x": "300 - 350", "y": 4},
    {"x": "350 - 400", "y": 4},
    {"x": "400 - 450", "y": 4},
    {"x": "450 - 500", "y": 1},
    {"x": "500 - 550", "y": 1}
]

# Extract x and y values
x = [r['x'] for r in ranges]
y = [int(r['y']) for r in ranges]

# Create subplots
fig, ax = plt.subplots(figsize=(10, 6))

# Create a bar chart on the first subplot
bars = ax.bar(x, y, color='grey')

# Add labels and title
ax.set_xlabel('Hidden Rank', fontweight='bold')
ax.set_ylabel('No. of Students', fontweight='bold')

# Add main title
plt.suptitle('Hidden Rank Distribution', fontsize=16, fontweight='bold', x=0.5)
plt.title('Before 1st Re-calibration (Agile)', fontsize=12, color='gray', x=0.5)

# Rotate x-axis labels for better visibility
ax.set_xticklabels(x, rotation=90, ha='right')

# Set y-axis limit to ensure all data points are visible
max_y = max(y)
ax.set_ylim(0, math.ceil(max_y / 20) * 20)

ax.yaxis.set_major_locator(MaxNLocator(integer=True))

# Add count as text to the top of each bar
for bar, count in zip(bars, y):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, count,
            ha='center', va='bottom', fontsize=10)

# Get the filename of the Python script
script_filename = os.path.splitext(os.path.basename(__file__))[0]

plt.tight_layout()
# Save the figure as a JPG with the same name as the Python script
plt.savefig(f'charts/agile/{script_filename}.jpg', dpi=1000)  # Set the resolution (dpi) as needed
