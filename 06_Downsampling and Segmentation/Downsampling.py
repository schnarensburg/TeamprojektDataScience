import trimesh
import numpy as np
import pandas as pd

# Load the .xyz file into a DataFrame
def load_xyz_file(file_path):
    df = pd.read_csv(file_path, delim_whitespace=True, header=None)
    return df

def downsample_point_cloud(df, n):
    """
    Downsample a point cloud by taking every nth point.
    """
    return df[::n]

df = load_xyz_file('/Users/aaronneumann/Documents/GitHub/TeamprojektDataScience/01_DATA/Z19/Z19 neu.xyz')

# Downsample the DataFrame
df_downsampled = downsample_point_cloud(df, 10)

# Convert dataframe to numpy array
points = df_downsampled.values

# Create a point cloud object
cloud = trimesh.points.PointCloud(points)

# Show the point cloud
cloud.show()
