import numpy as np
import open3d as o3d

# Load point clouds from .xyz files
cloud_file = "/Users/aaronneumann/Documents/GitHub/TeamprojektDataScience/01_DATA/Z19/PointClouds/.xyz/+01.xyz"  # Replace with your actual file names
reference_file = "/Users/aaronneumann/Documents/GitHub/TeamprojektDataScience/01_DATA/Z19/PointClouds/SollModelZ19.xyz"

cloud_data = np.loadtxt(cloud_file, skiprows=1)  # Assuming the file has header row
reference_data = np.loadtxt(reference_file, skiprows=1)

# Create Open3D point cloud objects
cloud_pcd = o3d.geometry.PointCloud()
reference_pcd = o3d.geometry.PointCloud()
cloud_pcd.points = o3d.utility.Vector3dVector(cloud_data[:, :3])
reference_pcd.points = o3d.utility.Vector3dVector(reference_data[:, :3])

#Align pointcloud models

o3d.pipelines.registration.registration_icp(cloud_pcd, reference_pcd,0.001)
# Visualize the point clouds with differences highlighted
o3d.visualization.draw_geometries([cloud_pcd, reference_pcd])


