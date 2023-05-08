import open3d as o3d
import numpy as np
#Read PointCloud 1+2
pcd1 = o3d.io.read_point_cloud("/Users/aaronneumann/Documents/GitHub/TeamprojektDataScience/resources/Kopfwelle_Z13/Kopfwelle_Serie_1/Messdaten/KW01.txt")
pcd2 = o3d.io.read_point_cloud("/Users/aaronneumann/Documents/GitHub/TeamprojektDataScience/resources/Kopfwelle_Z13/Kopfwelle_Serie_1/Messdaten/KW02.txt")
#Visualize Gears
o3d.visualization.draw_geometries([pcd1, pcd2])
#Calculate Distances between models
distances = pcd1.compute_point_cloud_distance(pcd2)
mean_distance = np.mean(distances)
max_distance = np.max(distances)
#Print results of measuring
print("Mean distance: ", mean_distance)
print("Max distance: ", max_distance)