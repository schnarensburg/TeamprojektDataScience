import csv

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

#Load 2dimCAD.csv
script_dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(script_dir, "../01_DATA/Z19/PointClouds/2dimZ19CAD.csv")

x = []
y = []

with open(file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        x.append(float(row[0]))
        y.append(float(row[1]))

plt.scatter(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('2D Coordinate Plot')
plt.grid(True)
plt.show()