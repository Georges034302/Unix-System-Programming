#!/usr/bin/env python3

"""
Compute projectile motion range.

Formula:
Range = (v^2 * sin(2θ)) / g

Concepts:
- trigonometry
- radians conversion
- mathematical modelling
"""

import math

# read input
v = float(input("Initial velocity (m/s): "))
angle = float(input("Angle (degrees): "))

# convert degrees → radians
theta = math.radians(angle)

# constant gravity
g = 9.8

# compute range
R = (v**2 * math.sin(2 * theta)) / g

print(f"\nRange = {R:.2f} meters")
