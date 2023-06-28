import open3d as o3d

def visualize_pointcloud_CAD(file_path):
    # Read xyz file and extract points
    points = []
    with open(file_path, 'r') as f:
        for line in f:
            x, y, z = line.split()
            points.append([float(x), float(y), float(z)])

    # Create Open3D pointcloud object
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(points)
    # Set visualization settings
    vis = o3d.visualization.Visualizer()
    vis.create_window()
    vis.add_geometry(point_cloud)
    render_option = vis.get_render_option()
    render_option.point_size = 3  # Adjust the size of the points
    render_option.show_coordinate_frame = True  # Show the coordinate frame

    # Run the visualization loop
    vis.run()
    vis.destroy_window()


visualize_pointcloud_CAD('/Users/aarongrommes/Library/CloudStorage/OneDrive-Persönlich/Studies/Semester 6/Teamprojekt/TeamprojektDataScience/TeamprojektDataScience/01_DATA/Z19/PointClouds/cutCADZ19.xyz')