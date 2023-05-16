import os
import csv

import numpy as np


def transform_point_cloud(point_cloud):
    transformed_points = []
    for point in point_cloud:
        # Discarding the y-coordinate (depth) and set it to zero
        transformed_point = [point[0], point[2]]
        transformed_points.append(transformed_point)
    return transformed_points


def save_transformed_point_cloud(transformed_points, output_file):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(transformed_points)


def main():
    dir_gear = os.path.dirname(os.path.abspath(__file__))
    gear_dir = os.path.join(dir_gear, "../01_DATA/Z19/PointClouds/MeiterradCutZ19.xyz")

    output_file = '2dimCAD.csv'

    point_cloud = np.loadtxt(gear_dir)

    transformed_points = transform_point_cloud(point_cloud)
    save_transformed_point_cloud(transformed_points, output_file)
    print("trafo completed")

    '''
    #Read the point cloud from input_file
    point_cloud = []
    with open(gear_dir, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            point = [float(row[0]), float(row[1]), float(row[2])]
            point_cloud.append(point)

    #Transform the point cloud
    transformed_points = transform_point_cloud(point_cloud)

    #Save the transformed point cloud
    save_transformed_point_cloud(transformed_points, output_file)

    print("Point cloud transformation complete!")
    '''


if __name__ == '__main__':
    main()
