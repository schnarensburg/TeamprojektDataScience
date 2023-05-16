import numpy as np
import open3d as o3d

meisterradZ19 = "/Users/aarongrommes/Library/CloudStorage/OneDrive-Persönlich/Studies/Semester 6/Teamprojekt/TeamprojektDataScience/TeamprojektDataScience/01_DATA/Z19/PointClouds/MeiterradCutZ19.xyz"
# INPUT 01_DATA / Load data from file
INPUTdata: object = np.loadtxt(meisterradZ19)

# Convert NumPy array to Open3D PointCloud object
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(INPUTdata)

# Create Open3D visualization window
o3d.visualization.draw_geometries([pcd])