import numpy as np
import open3d as o3d
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA

# Einlesen der Punktwolke
cloud = o3d.io.read_point_cloud("/Users/aarongrommes/Library/CloudStorage/OneDrive-Persönlich/Studies/Semester 6/Teamprojekt/TeamprojektDataScience/TeamprojektDataScience/01_DATA/Spanndorn/KW Spanndordn Fehlerteile nach Achsen Halt nach KW 76.xyz", format='xyz')

# Konvertieren in ein NumPy Array
points = np.asarray(cloud.points)

# DBSCAN Clustering
clustering = DBSCAN(eps=1, min_samples=10).fit(points)
unique_labels = np.unique(clustering.labels_)

# Teilen der Punktwolke in zwei Teile
points_cylinder1 = points[clustering.labels_ == unique_labels[0]]
points_cylinder2 = points[clustering.labels_ == unique_labels[1]]

# Konvertiere die Punkte zurück zu Open3D-Punktwolken
cloud_cylinder1 = o3d.geometry.PointCloud()
cloud_cylinder1.points = o3d.utility.Vector3dVector(points_cylinder1)
cloud_cylinder2 = o3d.geometry.PointCloud()
cloud_cylinder2.points = o3d.utility.Vector3dVector(points_cylinder2)

# Finden Sie die Hauptkomponenten der Punkte jedes Zylinders
pca = PCA(n_components=3)
pca.fit(points_cylinder1)
center_cylinder1 = pca.mean_
pca.fit(points_cylinder2)
center_cylinder2 = pca.mean_

# Erstelle Linien für die Mittelpunkte der Zylinder
lines = [[0, 1]]
colors = [[1, 0, 0] for i in range(len(lines))]
line_set = o3d.geometry.LineSet(
points=o3d.utility.Vector3dVector([center_cylinder1, center_cylinder2]),
lines=o3d.utility.Vector2iVector(lines),
)
line_set.colors = o3d.utility.Vector3dVector(colors)

# Visualisieren der Ergebnisse
o3d.visualization.draw_geometries([cloud_cylinder1, cloud_cylinder2, line_set])