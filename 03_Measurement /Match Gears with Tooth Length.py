import open3d as o3d
import numpy as np
import os

# Set paths to the Z13 and Z19 folders
z13_path = "/Users/aaronneumann/Documents/GitHub/TeamprojektDataScience/01_DATA/Z13/PointClouds/.xyz"
z19_path = "/Users/aaronneumann/Documents/GitHub/TeamprojektDataScience/01_DATA/Z19/PointClouds/.xyz"

# Get a list of all the .xyz files in the Z13 folder
z13_files = [f for f in os.listdir(z13_path) if f.endswith(".xyz")]

# Get a list of all the .xyz files in the Z19 folder
z19_files = [f for f in os.listdir(z19_path) if f.endswith(".xyz")]

# Create an empty results list
results = []

# Loop through all the gear pairs
for z13_file in z13_files:
    for z19_file in z19_files:
        # Load point cloud data for the first gear
        z13_pcd = o3d.io.read_point_cloud(os.path.join(z13_path, z13_file))

        # Load point cloud data for the second gear
        z19_pcd = o3d.io.read_point_cloud(os.path.join(z19_path, z19_file))

        # Align the point clouds to a common coordinate system using ICP
        icp_result = o3d.pipelines.registration.registration_icp(z13_pcd, z19_pcd, max_correspondence_distance=0.05)
        z19_pcd.transform(icp_result.transformation)

        # Segment the teeth of each gear using DBSCAN clustering
        eps = 0.05  # DBSCAN radius parameter
        min_pts = 10  # DBSCAN minimum number of points parameter
        z13_labels = np.array(o3d.ml.ops.cluster_dbscan(np.asarray(z13_pcd.points), eps, min_pts))
        z13_clusters = []
        for label in np.unique(z13_labels):
            if label == -1:
                continue
            cluster_mask = (z13_labels == label)
            z13_clusters.append(z13_pcd.select_by_index(np.where(cluster_mask)[0]))

        z19_labels = np.array(o3d.ml.ops.cluster_dbscan(np.asarray(z19_pcd.points), eps, min_pts))
        z19_clusters = []
        for label in np.unique(z19_labels):
            if label == -1:
                continue
            cluster_mask = (z19_labels == label)
            z19_clusters.append(z19_pcd.select_by_index(np.where(cluster_mask)[0]))

        # Compute the length of each tooth in both gears
        tooth_lengths_z13 = []
        for i in range(seg_z13.get_num_clusters()):
            cluster = clusters_z13[i]
            bbox = cluster.get_axis_aligned_bounding_box()
            length = bbox.get_max_bound()[0] - bbox.get_min_bound()[0]
            tooth_lengths_z13.append(length)

        tooth_lengths_z19 = []
        for i in range(seg_z19.get_num_clusters()):
            cluster = clusters_z19[i]
            bbox = cluster.get_axis_aligned_bounding_box()
            length = bbox.get_max_bound()[0] - bbox.get_min_bound()[0]
            tooth_lengths_z19.append(length)

        # Add the tooth lengths to the results list
        results.append((z13_file, z19_file, tooth_lengths_z13, tooth_lengths_z19))

# Write the results to a text file
with open("results.txt", "w") as f:
    for result in results:
        z13_file, z19_file, tooth_lengths_z13, tooth_lengths_z19 = result
        f.write(f"Gear pair: {z13_file} - {z19_file}\n")
        f.write(f"Z13 tooth lengths: {tooth_lengths_z13}\n")
        f.write(f"Z19 tooth lengths: {tooth_lengths_z19}\n")
        f.write("\n")