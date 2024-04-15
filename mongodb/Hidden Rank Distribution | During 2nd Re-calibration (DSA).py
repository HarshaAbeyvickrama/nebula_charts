import math
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Sample data
ranges = [
  { "x": "-750 - -600", "y": 2 },
  { "x": "-450 - -300", "y": 1 },
  { "x": "-300 - -150", "y": 2 },
  { "x": "-150 - 0", "y": 5 },
  { "x": "0 - 150", "y": 14 },
  { "x": "150 - 300", "y": 11 },
  { "x": "300 - 450", "y": 4 },
  { "x": "450 - 600", "y": 5 },
  { "x": "600 - 750", "y": 3 },
  { "x": "750 - 900", "y": 5 },
  { "x": "900 - 1,050", "y": 6 },
  { "x": "1,050 - 1,200", "y": 2 }
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
plt.title('During 2nd Re-calibration (DSA)', fontsize=12, color='gray', x=0.5)

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
plt.savefig(f'charts/{script_filename}.jpg', dpi=1000)  # Set the resolution (dpi) as needed
