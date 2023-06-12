import scipy.io as sio
import numpy as np

# Lade die .mat-Datei
data = sio.loadmat(
    "/Users/moritz/PycharmProjects/TeamprojektDataScience/01_DATA/CAD_Modell_Z13/CAD_Modell_ROI_100000_ausgerichtet.mat")

# Erhalte die Punktewolkenkoordinaten
pointCloud = data["ptCloudCAD_cut"]  # Annahme: Die Punktewolke befindet sich in der Variable "pointCloud"

# Schreibe die Punktewolkenkoordinaten in eine Textdatei
np.savetxt('point_cloud.txt', pointCloud, delimiter=' ', fmt='%f')
