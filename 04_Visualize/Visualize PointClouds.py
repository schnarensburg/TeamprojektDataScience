import numpy as np
import open3d as o3d

# INPUT 01_DATA / Load data from file
INPUTdata: object = np.loadtxt(
    '/00_GENERAL/resources/Kopfwelle_Z13/Transformed data/KW20_Data.xyz')

# Convert NumPy array to Open3D PointCloud object
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(INPUTdata)

# Create Open3D visualization window
o3d.visualization.draw_geometries([pcd])