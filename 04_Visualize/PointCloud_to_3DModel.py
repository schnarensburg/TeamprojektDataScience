import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os



#Load MeisterradCutZ19
script_dir = os.path.dirname(os.path.abspath(__file__))
#file_path = os.path.join(script_dir, "../01_DATA/Z19/PointClouds/cutCAD_Z13.xyz")
file_path = '/Users/aarongrommes/Library/CloudStorage/OneDrive-Persönlich/Studies/Semester 6/Teamprojekt/TeamprojektDataScience/TeamprojektDataScience/04_Visualize/PointCloud_to_3DModel.py'
cloud_data = np.loadtxt(file_path)

#Seperate coordinates in individual arrays
x = cloud_data[:, 0]
y = cloud_data[:, 1]
z = cloud_data[:, 2]

#Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#Create a scatter plot of the pointcloud
ax.scatter(x, y, z, s=1)

plt.show()

