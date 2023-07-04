import open3d as o3d
import numpy as np

# Load point cloud data for the gear
gear_pcd = o3d.geometry.PointCloud()
gear_points: object = np.loadtxt("/Users/aaronneumann/Documents/GitHub/TeamprojektDataScience/01_DATA/Z19/PointClouds/.xyz/+95.xyz")
gear_pcd.points = o3d.utility.Vector3dVector(gear_points)

# Load point cloud data for the reference model
reference_pcd = o3d.geometry.PointCloud()
reference_points : object = np.loadtxt("/Users/aaronneumann/Documents/GitHub/TeamprojektDataScience/01_DATA/Z19/PointClouds/.xyz/+96.xyz")
pcd = o3d.geometry.PointCloud()
reference_pcd.points = o3d.utility.Vector3dVector(reference_points)

# Preprocess the point clouds if necessary

# Perform registration using ICP
icp_result = o3d.pipelines.registration.registration_icp(gear_pcd, reference_pcd, max_correspondence_distance=0.05)
gear_pcd.transform(icp_result.transformation)

# Compute distances between corresponding points
distances = np.asarray(gear_pcd.compute_point_cloud_distance(reference_pcd))

# Set a threshold to classify points as different
threshold = 0.00001  # Adjust this value based on your data
different_points = distances - threshold
# Create a mask to identify different points


# Visualize the gear point cloud with highlighted differences
gear_pcd.paint_uniform_color([1, 0, 0])  # Color all points red
gear_pcd.colors[different_points] = [0, 1, 0]  # Color different points green

# Visualize the point cloud
o3d.visualization.draw_geometries([gear_pcd],)

