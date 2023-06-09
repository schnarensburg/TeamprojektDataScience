import numpy as np
import open3d as o3d
import os


# INPUT 01_DATA / Load data from file
script_dir = os.path.dirname(os.path.abspath(__file__))
#file_path = os.path.join(script_dir, "../01_DATA/Z19/PointClouds/.csv2D/+01_2D.csv")
file_path = '/Users/aarongrommes/Library/CloudStorage/OneDrive-Persönlich/Studies/Semester 6/Teamprojekt/TeamprojektDataScience/TeamprojektDataScience/01_DATA/Z13/PointClouds/cutCAD_Z13.xyz'

INPUTdata: object = np.loadtxt(file_path)

# Convert NumPy array to Open3D PointCloud object
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(INPUTdata)

# Create Open3D visualization window
o3d.visualization.draw_geometries([pcd])
