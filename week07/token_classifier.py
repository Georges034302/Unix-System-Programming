#!/usr/bin/env python3

x = int(input("x: "))
y = int(input("y: "))

# --- Position ---
# Check the special cases first, then the four quadrants
if x == 0 and y == 0:
    position = "Origin"
elif y == 0:
    position = "X-axis"
elif x == 0:
    position = "Y-axis"
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

