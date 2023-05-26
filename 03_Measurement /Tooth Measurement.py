import os
import open3d as o3d
import numpy as np

#Problematic due to different sizes. Segmentation algorithm cant stack the gears and test.

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
pcd1.points = o3d.utility.Vector3dVector(np.concatenate([np.asarray(pcd.points) for pcd in pcd1_list], axis=0))


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
icp_result = o3d.pipelines.registration.registration_icp(pcd1, pcd2, max_correspondence_distance=0.05)
pcd2.transform(icp_result.transformation)

# Segment the teeth of each gear using region growing - Problematic
seg1 = pcd1.segment_plane(distance_threshold=0.02, ransac_n=3, num_iterations=100)
pcd1 = pcd1.select_by_index(seg1.inliers, invert=True)

seg2 = pcd2.segment_plane(distance_threshold=0.02, ransac_n=3, num_iterations=100)
pcd2 = pcd2.select_by_index(seg2.inliers, invert=True)

clusters1, _ = o3d.geometry.cluster_dbscan(pcd1, eps=0.02, min_points=10, print_progress=False)
clusters2, _ = o3d.geometry.cluster_dbscan(pcd2, eps=0.02, min_points=10, print_progress=False)



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