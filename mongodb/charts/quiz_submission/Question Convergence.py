import os
import math
import matplotlib.pyplot as plt
import numpy as np

# Sample data
ranges = [
    {"x": 32, "y_series_0": 750, "y": 399.91520633126083},
    {"x": 28, "y_series_0": 750, "y": 449.0955342001132},
    {"x": 7, "y_series_0": 750, "y": 685.344827586207},
    {"x": 3, "y_series_0": 750, "y": 737.0689655172414},
    {"x": 25, "y_series_0": 750, "y": 485.9807801017525},
    {"x": 13, "y_series_0": 750, "y": 635.7758620689656},
    {"x": 27, "y_series_0": 750, "y": 461.3906161673263},
    {"x": 1, "y_series_0": 750, "y": 737.0689655172414},
    {"x": 17, "y_series_0": 750, "y": 585.7758620689656},
    {"x": 9, "y_series_0": 750, "y": 685.7758620689656},
    {"x": 26, "y_series_0": 750, "y": 473.6856981345394},
    {"x": 31, "y_series_0": 750, "y": 412.2102882984739},
    {"x": 12, "y_series_0": 750, "y": 648.2758620689656},
    {"x": 21, "y_series_0": 750, "y": 535.7758620689656},
    {"x": 38, "y_series_0": 750, "y": 351.3298017834025},
    {"x": 22, "y_series_0": 750, "y": 523.2758620689656},
    {"x": 37, "y_series_0": 750, "y": 363.4265759769509},
    {"x": 20, "y_series_0": 750, "y": 548.2758620689656},
    {"x": 39, "y_series_0": 750, "y": 339.2330275898541},
    {"x": 6, "y_series_0": 750, "y": 698.2758620689656},
    {"x": 11, "y_series_0": 750, "y": 660.7758620689656},
    {"x": 16, "y_series_0": 750, "y": 598.2758620689656},
    {"x": 4, "y_series_0": 750, "y": 724.1379310344828},
    {"x": 19, "y_series_0": 750, "y": 560.7758620689656},
    {"x": 35, "y_series_0": 750, "y": 387.62012436404774},
    {"x": 2, "y_series_0": 750, "y": 724.1379310344828},
    {"x": 10, "y_series_0": 750, "y": 673.2758620689656},
    {"x": 34, "y_series_0": 750, "y": 375.32504239683465},
    {"x": 36, "y_series_0": 750, "y": 375.5233501704993},
    {"x": 23, "y_series_0": 750, "y": 510.7758620689656},
    {"x": 24, "y_series_0": 750, "y": 498.2758620689656},
    {"x": 5, "y_series_0": 750, "y": 711.2068965517242},
    {"x": 29, "y_series_0": 750, "y": 436.8004522329001},
    {"x": 30, "y_series_0": 750, "y": 424.505370265687},
    {"x": 33, "y_series_0": 750, "y": 387.62012436404774},
    {"x": 18, "y_series_0": 750, "y": 573.2758620689656},
    {"x": 8, "y_series_0": 750, "y": 698.2758620689656},
    {"x": 14, "y_series_0": 750, "y": 623.2758620689656},
    {"x": 15, "y_series_0": 750, "y": 610.7758620689656}
]

# Extract x, y_series_0, and y values
x = [r['x'] for r in ranges]
y_series_0 = [r['y_series_0'] for r in ranges]
y = [r['y'] for r in ranges]

# Sort x
ranges_sorted = sorted(ranges, key=lambda x: x['x'])
x = [r['x'] for r in ranges_sorted]
y_series_0 = [r['y_series_0'] for r in ranges_sorted]
y = [r['y'] for r in ranges_sorted]

# Create subplots
fig, ax = plt.subplots(figsize=(10, 6))

# Create line chart for y_series_0 against x
line1 = ax.plot(x, y_series_0, color='green', marker='o', linestyle='-', label='Initial Difficulty')

# Create line chart for y against x
line2 = ax.plot(x, y, color='blue', marker='o', linestyle='-', label='Difficulty')

# Add labels and title
ax.set_xlabel('No. of Attempts', fontweight='bold')
ax.set_ylabel('Difficulty', fontweight='bold')

# Add main title
plt.suptitle('Question Convergence', fontsize=16, fontweight='bold', x=0.5)
plt.title('Initial Difficulty vs Difficulty Evolution', fontsize=12, color='gray', x=0.5)

# Set x-axis limits to ensure all data points are visible
ax.set_xlim(min(x), max(x))

# Rotate x-axis labels for better visibility
# ax.set_xticklabels(x, rotation=90, ha='right')

# Add a legend
ax.legend()

# Set y-axis limit to ensure all data points are visible
max_y = max(y)
ax.set_ylim(0, 1500)

# Fit a logarithmic regression line (trend line) for y_series_0
z_series_0 = np.polyfit(x, np.log(y), 1)  # Fit a logarithmic regression
p_series_0 = np.poly1d(z_series_0)  # Create a polynomial function
plt.plot(x, np.exp(p_series_0(x)), 'r--', label='Trend Line (Logarithmic Difficulty)')

# Add a legend for the trend line
plt.legend()

# Adjust layout
plt.tight_layout()

# Get the filename of the Python script
script_filename = os.path.splitext(os.path.basename(__file__))[0]

# Save the figure as a JPG with the same name as the Python script
plt.savefig(f'{script_filename}.jpg', dpi=1000)  # Set the resolution (dpi) as needed

