import numpy as np
import matplotlib.pyplot as plt
import os
import math


def visualize_2d_txt(txt_file, title):
    # Read the contents of TXT file
    with open(txt_file, 'r') as file:
        lines = file.readlines()

    # Extract X and Y values
    x_values = []
    y_values = []
    for line in lines:
        x, y = map(float, line.split())
        x_values.append(x)
        y_values.append(y)

    # Plot the data
    plt.scatter(x_values, y_values)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(title)
    plt.legend()




script_dir1 = os.path.dirname(os.path.abspath(__file__))
file1 = os.path.join(script_dir1, '../01_DATA/Z19/PointClouds/2dimZ19CAD.txt')

plt.figure()

visualize_2d_txt(file1, '+01_2D.txt')

plt.show()

