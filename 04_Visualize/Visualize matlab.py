from scipy.io import loadmat
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# .mat-Datei laden
data = loadmat('/Users/aaronneumann/Documents/GitHub/TeamprojektDataScience/01_DATA/Matlab/CAD_Modell_ROI_100000_ausgerichtet.mat')

# Punktkoordinaten extrahieren
points = data[100000]

# Punktwolke plotten
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:, 0], points[:, 1], points[:, 2])
plt.show()