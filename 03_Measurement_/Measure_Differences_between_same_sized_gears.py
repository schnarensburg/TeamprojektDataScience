import open3d as o3d
import numpy as np
#Read PointCloud 1+2
#original path pcd1:/00_GENERAL/resources/Kopfwelle_Z13/Transformed data/KW20_Data.xyz
#path pcd2: /visualisation/Compare PointClouds/OUTPUT_Z19_.xyz/+01.xyz

kw01Z13 = '/Users/aarongrommes/Library/CloudStorage/OneDrive-Persönlich/Studies/Semester 6/Teamprojekt/TeamprojektDataScience/TeamprojektDataScience/00_GENERAL/resources/Kopfwelle_Z13/Transformed data/xyzFormat/KW01.xyz'
kw02Z13 = '/Users/aarongrommes/Library/CloudStorage/OneDrive-Persönlich/Studies/Semester 6/Teamprojekt/TeamprojektDataScience/TeamprojektDataScience/00_GENERAL/resources/Kopfwelle_Z13/Transformed data/xyzFormat/KW02.xyz'


pcd1 = o3d.io.read_point_cloud(kw01Z13)

pcd2 = o3d.io.read_point_cloud(kw02Z13)
#Visualize Gears
color1 = [1, 0, 0] #red
color2 = [0, 1, 0] #green

o3d.visualization.draw_geometries([pcd1, pcd2])
#Calculate Distances between models
distances = pcd1.compute_point_cloud_distance(pcd2)
mean_distance = np.mean(distances)
max_distance = np.max(distances)
#Print results of measuring
print("Mean distance: ", mean_distance)
print("Max distance: ", max_distance)