import math
import os
import matplotlib.pyplot as plt

# Sample data
ranges = [
    {"x": "0 - 150", "y": 5},
    {"x": "150 - 300", "y": 3},
    {"x": "300 - 450", "y": 4},
    {"x": "450 - 600", "y": 8},
    {"x": "600 - 750", "y": 9},
    {"x": "750 - 900", "y": 13},
    {"x": "900 - 1,050", "y": 8},
    {"x": "1,050 - 1,200", "y": 8},
    {"x": "1,200 - 1,350", "y": 3},
    {"x": "1,350 - 1,500", "y": 1}
]

# Extract x and y values
x = [r['x'] for r in ranges]
y = [r['y'] for r in ranges]

# Create subplots
fig, ax = plt.subplots(figsize=(10, 6))

# Create a bar chart on the first subplot
bars = ax.bar(x, y, color='blue')


# Add labels and title
ax.set_xlabel('Student Hidden Rank', fontweight='bold')
ax.set_ylabel('Student Count', fontweight='bold')
ax.set_title('Student Count by Public Rank', fontweight='bold')

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
