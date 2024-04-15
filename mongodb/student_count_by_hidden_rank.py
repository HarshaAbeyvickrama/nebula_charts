import math
import os
import matplotlib.pyplot as plt

# Sample data
ranges = [
    {"x": "-750 - -600", "ylines": 2, "y": 2},
    {"x": "-450 - -300", "ylines": 1, "y": 1},
    {"x": "-300 - -150", "ylines": 2, "y": 2},
    {"x": "-150 - 0", "ylines": 7, "y": 7},
    {"x": "0 - 150", "ylines": 14, "y": 14},
    {"x": "150 - 300", "ylines": 11, "y": 11},
    {"x": "300 - 450", "ylines": 4, "y": 4},
    {"x": "450 - 600", "ylines": 4, "y": 4},
    {"x": "600 - 750", "ylines": 4, "y": 4},
    {"x": "750 - 900", "ylines": 5, "y": 5},
    {"x": "900 - 1,050", "ylines": 6, "y": 6},
    {"x": "1,050 - 1,200", "ylines": 2, "y": 2}
]

# Extract x and y values
x = [r['x'] for r in ranges]
y = [r['y'] for r in ranges]
ylines = [r['ylines'] for r in ranges]

# Create subplots
fig, ax = plt.subplots(figsize=(10, 6))

# Create a bar chart on the first subplot
bars = ax.bar(x, y, color='green')

# Add line connectors on the first subplot
for i in range(len(x) - 1):
    x_pos = [(bars[i].get_x() + bars[i].get_width() / 2),
             (bars[i + 1].get_x() + bars[i + 1].get_width() / 2)]
    y_pos = [y[i], y[i + 1]]
    ax.plot(x_pos, y_pos, color='red', linestyle='-', linewidth=0.5)

# Add labels and title
ax.set_xlabel('Student Hidden Rank', fontweight='bold')
ax.set_ylabel('Student Count', fontweight='bold')
ax.set_title('Student Count by Hidden Rank', fontweight='bold')

# Rotate x-axis labels for better visibility
ax.set_xticklabels(x, rotation=45, ha='right')

# Set y-axis limit to ensure all data points are visible
max_y = max(y)
ax.set_ylim(0, math.ceil(max_y / 20) * 20)

# Get the filename of the Python script
script_filename = os.path.splitext(os.path.basename(__file__))[0]

plt.tight_layout()
# Save the figure as a JPG with the same name as the Python script
plt.savefig(f'charts/{script_filename}.jpg', dpi=1000)  # Set the resolution (dpi) as needed

