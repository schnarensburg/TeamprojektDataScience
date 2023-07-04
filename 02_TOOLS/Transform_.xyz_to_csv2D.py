import os
import csv
import numpy as np

dir_in = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(dir_in, '../01_DATA/Z13/PointClouds/.xyz')

dir_out = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(dir_out, '../01_DATA/Z13/PointClouds/.csv2D')

for filename in os.listdir(input_folder):
    if filename.endswith('.xyz'):
        with open(os.path.join(input_folder, filename), 'r') as file:
            pointcloud = np.loadtxt(file)

        transformed_points = []
        for point in pointcloud:
            # Discarding the y-coordinate (depth) and set it to zero
            transformed_point = [point[0], point[2]]
            transformed_points.append(transformed_point)

        new_csv = os.path.join(output_folder, filename.replace('.xyz', '.csv'))

        with open(new_csv, 'w', newline='') as newfile:
            writer = csv.writer(newfile)
            writer.writerows(transformed_points)


