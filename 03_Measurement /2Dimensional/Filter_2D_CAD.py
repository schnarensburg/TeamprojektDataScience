import os

import matplotlib.pyplot as plt
import numpy as np


def filter_points_by_radius(point_cloud, inner_radius, outer_radius):
    filtered_points = []

    for point in point_cloud:
        distance = (point[0]**2 + point[1]**2)**0.5
        if inner_radius <= distance <= outer_radius:
            filtered_points.append(point)

    return filtered_points
def plot_point_cloud(point_cloud):
    x = [point[0] for point in point_cloud]
    y = [point[1] for point in point_cloud]

    plt.scatter(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Filtered Point Cloud')
    plt.show()

dir = os.path.dirname(__file__)
file_path = os.path.join(dir, '../../01_DATA/Z19/PointClouds/2dimZ19CAD.txt')
outer_radius = 0.0035*1000
inner_radius = 0.0021*1000


point_cloud = np.loadtxt(file_path)
plot_point_cloud(filter_points_by_radius(point_cloud, inner_radius, outer_radius))
