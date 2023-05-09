import os
import open3d as o3d

# Set the input directories for each gear
gear1_dir = "/Users/aaronneumann/Documents/GitHub/TeamprojektDataScience/01_DATA/Z13/PointClouds/.xyz" #Z13
gear2_dir = "/Users/aaronneumann/Documents/GitHub/TeamprojektDataScience/01_DATA/Z19/PointClouds/.xyz" #Z19

# Load point cloud data for the first gear
gear1_files = sorted(os.listdir(gear1_dir))
pcd1_list = []
for file in gear1_files:
    if file.endswith(".xyz"):
        pcd1 = o3d.io.read_point_cloud(os.path.join(gear1_dir, file))
        pcd1_list.append(pcd1)
pcd1 = o3d.geometry.PointCloud()
pcd1.points = o3d.utility.Vector3dVector(np.concatenate([pcd.points for pcd in pcd1_list], axis=0))

# Load point cloud data for the second gear
gear2_files = sorted(os.listdir(gear2_dir))
pcd2_list = []
for file in gear2_files:
    if file.endswith(".xyz"):
        pcd2 = o3d.io.read_point_cloud(os.path.join(gear2_dir, file))
        pcd2_list.append(pcd2)
pcd2 = o3d.geometry.PointCloud()
pcd2.points = o3d.utility.Vector3dVector(np.concatenate([pcd.points for pcd in pcd2_list], axis=0))

# Align the point clouds to a common coordinate system using ICP
icp_result = o3d.registration.registration_icp(pcd1, pcd2, max_correspondence_distance=0.05)
pcd2.transform(icp_result.transformation)

# Segment the teeth of each gear using region growing
seg1 = o3d.geometry.PointCloudSegmentation.create_from_point_cloud_with_radius(pcd1, 0.02)
seg1.extract_clusters(min_points=10, max_points=100000)
clusters1 = seg1.get_cluster_point_clouds()

seg2 = o3d.geometry.PointCloudSegmentation.create_from_point_cloud_with_radius(pcd2, 0.02)
seg2.extract_clusters(min_points=10, max_points=100000)
clusters2 = seg2.get_cluster_point_clouds()

# Compute the length of each tooth in both gears
tooth_lengths1 = []
for cluster in clusters1:
    bbox = cluster.get_axis_aligned_bounding_box()
    length = bbox.get_max_bound()[0] - bbox.get_min_bound()[0]
    tooth_lengths1.append(length)

tooth_lengths2 = []
for cluster in clusters2:
    bbox = cluster.get_axis_aligned_bounding_box()
    length = bbox.get_max_bound()[0] - bbox.get_min_bound()[0]
    tooth_lengths2.append(length)

# Print the lengths of the teeth for each gear
print("Gear 1 tooth lengths:", tooth_lengths1)
print("Gear 2 tooth lengths:", tooth_lengths2)