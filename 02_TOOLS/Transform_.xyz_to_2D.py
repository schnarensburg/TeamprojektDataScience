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
    gear_dir = os.path.join(dir_gear, "../01_DATA/Z13/PointClouds/.xyz/KW01.xyz")

    output_file = '../01_DATA/Z13/PointClouds/.csv2D/KW012D.csv'

    point_cloud = np.loadtxt(gear_dir)

    transformed_points = transform_point_cloud(point_cloud)
    save_transformed_point_cloud(transformed_points, output_file)
    print("trafo completed")


if __name__ == '__main__':
    main()
