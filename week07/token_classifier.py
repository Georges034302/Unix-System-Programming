#!/usr/bin/env python3
"""
Find the position and distance of a point on a coordinate plane.

Usage:
    python3 token_classifier.py
    Enter the integer x and y coordinates when prompted.
"""

x = int(input("x: "))  # Read the horizontal coordinate.
y = int(input("y: "))  # Read the vertical coordinate.

# --- Position ---
# Check the special cases first, then the four quadrants
if x == 0 and y == 0:
    position = "Origin"  # Both coordinates are zero.
elif y == 0:
    position = "X-axis"  # The point lies on the horizontal axis.
elif x == 0:
    position = "Y-axis"  # The point lies on the vertical axis.
elif x > 0 and y > 0:
    position = "Quadrant I"    # (+, +)
elif x < 0 and y > 0:
    position = "Quadrant II"   # (-, +)
elif x < 0 and y < 0:
    position = "Quadrant III"  # (-, -)
else:
    position = "Quadrant IV"   # (+, -)

# --- Distance from origin ---
# Pythagorean theorem: sqrt(x² + y²)
distance = ((x ** 2) + (y ** 2)) ** 0.5

# --- Output ---
print(f"Coordinate : ({x}, {y})")
print(f"Position   : {position}")
print(f"Distance   : {distance:.2f}")

print(f"Position   : {position}")
print(f"Distance   : {distance:.2f}")
