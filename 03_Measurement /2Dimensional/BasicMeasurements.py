import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file1 = os.path.join(script_dir, "../01_DATA/Z13/PointClouds/.txt2D/KW01_2D.txt")
file1 = '/Users/aarongrommes/Library/CloudStorage/OneDrive-Persönlich/Studies/Semester 6/Teamprojekt/TeamprojektDataScience/TeamprojektDataScience/01_DATA/Z13/PointClouds/2dimZ13CAD.csv'
gear1 = np.loadtxt(file1, dtype=float)

file2 = '/Users/aarongrommes/Library/CloudStorage/OneDrive-Persönlich/Studies/Semester 6/Teamprojekt/TeamprojektDataScience/TeamprojektDataScience/01_DATA/Z13/PointClouds/.txt2D/KW02_2D.txt'
gear2 = np.loadtxt(file2, dtype=float)

diff = np.abs(gear1 - gear2)
mean_diff = np.mean(diff)
max_diff = np.max(diff)
min_diff = np.min(diff)

print(f"Mean Difference: {mean_diff}")
print(f"Maximum Difference: {max_diff}")
print(f"Minimum Difference: {min_diff}")