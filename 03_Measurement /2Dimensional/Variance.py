import math
import os
import numpy as np


def calculate_means(txt2D_folder, z13CAD):
    means_array = []
    file_list = os.listdir(txt2D_folder)

    for file in file_list:
        file_name = os.path.join(txt2D_folder, file)

        sum = 0
        j = 0
        for tooth in range(1, 13):
            j += 1
            tooth_pc = get_current_tooth(file_name, j)
            tooth_CAD = get_current_tooth(z13CAD, j)
            for point1, point2 in zip(tooth_pc, tooth_CAD):
                x1, y1 = point1
                x2, y2 = point2
                sum += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        mean = sum / 13
        means_array.append([file, mean])

    print(means_array)

def get_current_tooth(file, j):
    corridor_angle = ((j+0.25) * 360/13, (j+1.25)*360/13)
    with open(file, 'r') as file:
        lines = file.readlines()

        # Extract X and Y for points within the area
        points = []

        for line in lines:
            x, y = map(float, line.split())
            angle = math.atan2(y, x)
            if angle < 0:
                angle += 2 * math.pi

            angle_degrees = math.degrees(angle)
            if corridor_angle[0] <= angle_degrees <= corridor_angle[1]:
                points.append([x, y])
    return np.array(points)

txt2D_folder = '/Users/aarongrommes/Library/CloudStorage/OneDrive-Persönlich/Studies/Semester 6/Teamprojekt/TeamprojektDataScience/TeamprojektDataScience/01_DATA/Z13/PointClouds/.txt2D'
Z13CAD = '/Users/aarongrommes/Library/CloudStorage/OneDrive-Persönlich/Studies/Semester 6/Teamprojekt/TeamprojektDataScience/TeamprojektDataScience/01_DATA/Z13/PointClouds/2dimZ13CAD.txt'
calculate_means(txt2D_folder, Z13CAD)