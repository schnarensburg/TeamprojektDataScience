from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from scipy.spatial import ConvexHull
import numpy as np
import math
import os.path
import matplotlib.pyplot as plt

def get_outer_shape(point_cloud):
    # Compute convex hull of the point cloud
    hull = ConvexHull(point_cloud)

    # Retrieve outer shape points
    outer_shape_points = point_cloud[hull.vertices]

    return outer_shape_points


def visualize_outer_shape(point_cloud, outer_shape_points):
    plt.scatter(point_cloud[:, 0], point_cloud[:, 1], c='b', alpha=0.5, label='Point Cloud')

    # Plot outer shape
    plt.scatter(outer_shape_points[:, 0], outer_shape_points[:, 1], c='r', marker='o', label='Outer Shape')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()


dir = os.path.dirname(__file__)
file_path = os.path.join(dir, '../../01_DATA/Z19/PointClouds/.txt2D/+01_2D.txt')
gear_center = (0, 0)
gear_radius = 0.0035

#draw_gear_outline(file_path, gear_center)

point_cloud = np.loadtxt(file_path)
outer_shape = get_outer_shape(point_cloud)
visualize_outer_shape(point_cloud, outer_shape)
