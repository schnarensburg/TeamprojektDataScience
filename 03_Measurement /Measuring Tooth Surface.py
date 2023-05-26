import numpy as np
from scipy.spatial import Delaunay

def calculate_tooth_areas(points):
    # Delaunay-Triangulation durchführen
    tri = Delaunay(points)

    # Dreiecke abrufen
    triangles = tri.points[tri.simplices]

    # Umformen der Dreiecks-Koordinaten
    triangles_reshaped = triangles.transpose((0, 2, 1))

    # Fläche jedes Dreiecks berechnen
    areas = 0.5 * np.linalg.norm(np.cross(triangles_reshaped[:, 1] - triangles_reshaped[:, 0], triangles_reshaped[:, 2] - triangles_reshaped[:, 0]), axis=1)

    return areas

# Dateipfad zur .xyz-Datei
file_path = '/Users/aaronneumann/Documents/GitHub/TeamprojektDataScience/01_DATA/Z19/PointClouds/.xyz/+90.xyz'

# Lese die .xyz-Datei und speichere die Koordinaten in einem NumPy-Array
points = np.loadtxt(file_path, skiprows=1)

# Fläche jedes Zahnes berechnen
tooth_areas = calculate_tooth_areas(points)

# Ausgabe der Fläche jedes Zahnes
for i, area in enumerate(tooth_areas):
    print("Fläche Zahn", i+1, ":", area)