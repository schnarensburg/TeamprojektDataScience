import numpy as np
import matplotlib.pyplot as plt
import os

def visualize_2d_txt(txt_file):
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

    plt.scatter(x_values, y_values)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('2D Plot')
    plt.show()


script_dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(script_dir, "../01_DATA/Z13/PointClouds/.txt2D/KW01_2D.txt")
visualize_2d_txt(file)