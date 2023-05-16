import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import DBSCAN

# INPUT 01_DATA / Load data from file
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "../01_DATA/Z19/PointClouds/MeiterradCutZ19.xyz")

#Load and separate data
gear_data = np.loadtxt(file_path)
x = gear_data[:, 0]
y = gear_data[:, 1]
z = gear_data[:, 2]

feature_matrix = np.column_stack((x, y, z))
dbscan = DBSCAN(eps=0.1, min_samples=10)
labels = dbscan.fit_predict(feature_matrix)

unique_labels = np.unique(labels)

tooth_index = 0
tooth_points = feature_matrix[labels == unique_labels[tooth_index]]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(tooth_points[:, 0], tooth_points[:, 1], tooth_points[:, 2], s=20)

plt.show()

