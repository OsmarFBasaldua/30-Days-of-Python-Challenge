# 1. Write an example for different Pyhton data types such as Number (Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

# answer
print(type(100)) # int
print(type(10.50)) # float
print(type(1 + 2j)) # complex
print(type("This is a String")) # string
print(type(True)) # boolean
print(type([1, 2, 3, 4, 5])) # list 
print(type((1, 2, 3, 4, 5))) # tuple
print(type({1, 2, 3, 4, 5})) # set
print(type({"name": "Osmar", "age": 30, "country": "Mexico"})) # dictionary

# 2. Find an Euclidean distance between (2, 3) and (10, 8)
# Investigate the formula: sqrt((x2 - x1)^2 + (y2 - y1)^2) where (x1, y1) and (x2, y2) are the coordinates of the two points.
# https://docs.python.org/es/3.14/library/math.html#math.sqrt


'''Aswer / documentation oficial of python.''' 

import math # Import the math module to use the sqrt function. sqrt is used to calculate the square root, which is necessary for finding the Euclidean distance.

# Define points a and b as tuples representing their coordinates in a 2D space. Point a has coordinates (2, 3) and point b has coordinates (10, 8).
a = (2, 3)
b = (10, 8)

# Calculate the Euclidean distance between points a and b using the formula: sqrt(sum((px - qx) ** 2.0 for px, qx in zip(a, b))).
distance = math.sqrt(sum((px - qx) ** 2.0 for px, qx in zip(a, b)))
print(f"Euclidean distance between {a} and {b} is {distance}")


