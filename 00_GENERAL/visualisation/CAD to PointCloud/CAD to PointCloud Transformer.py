#Import open 3d package
import open3d as o3d
#from open3d.geometry import PointCloud

# Adjust number of point in point cloud
numberofpoints=1000000
#INPUT and READ CAD model
mesh = o3d.io.read_triangle_mesh("/resources/Kopfwelle_Z13/Transformed data/Z19.stl")
#Convert to PointCloud
point_cloud = mesh.sample_points_uniformly(number_of_points=numberofpoints)
#Visual Pointcloud
o3d.visualization.draw_geometries([point_cloud])
#Save file as pointcloud in designated file.
o3d.io.write_point_cloud("point_cloud_from_cad.xyz", point_cloud) # replace "point_cloud.pcd" with the desired name and path for your output file
