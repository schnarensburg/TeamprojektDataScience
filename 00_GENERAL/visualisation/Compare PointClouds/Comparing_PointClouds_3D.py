import open3d as o3d
import numpy as np
#Read PointCloud 1+2
#original path pcd1:

pcd1 = o3d.io.read_point_cloud("/00_GENERAL/resources/Kopfwelle_Z13/Transformed data/KW20_Data.xyz")
pcd2 = o3d.io.read_point_cloud("/visualisation/Compare PointClouds/OUTPUT_Z19_.xyz/+01.xyz")
#Visualize Gears
o3d.visualization.draw_geometries([pcd1, pcd2])
#Calculate Distances between models
distances = pcd1.compute_point_cloud_distance(pcd2)
mean_distance = np.mean(distances)
max_distance = np.max(distances)
#Print results of measuring
print("Mean distance: ", mean_distance)
print("Max distance: ", max_distance)