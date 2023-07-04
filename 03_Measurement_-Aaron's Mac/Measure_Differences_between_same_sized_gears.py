import open3d as o3d
import numpy as np
#Read PointCloud 1+2
#original path pcd1:

pcd1 = o3d.io.read_point_cloud("/Users/aaronneumann/Documents/GitHub/TeamprojektDataScience/01_DATA/Z13/PointClouds/.xyz/KW01.xyz")
pcd2 = o3d.io.read_point_cloud("/Users/aaronneumann/Documents/GitHub/TeamprojektDataScience/01_DATA/Z19/PointClouds/.xyz/+02.xyz")
#Visualize Gears
o3d.visualization.draw_geometries([pcd1, pcd2])
#Calculate Distances between models
distances = pcd1.compute_point_cloud_distance(pcd2)
mean_distance = np.mean(distances)
max_distance = np.max(distances)
#Print results of measuring
print("Mean distance: ", mean_distance)
print("Max distance: ", max_distance)