# Diese Datei soll die Messergebnisse aus https://github.com/schnarensburg/TeamprojektDataScience/blob/119e50018b0d7991617358bff47089cf499fa27c/resources/Kopfwelle_Z13/Kopfwelle_Serie_1/Messdaten
# visualisieren und möglichst in einer 3D Punktewolke darstellen
#see: https://stackoverflow.com/questions/38532298/how-can-you-plot-data-from-a-txt-file-using-matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

kw01 = pd.read_csv('/Users/aarongrommes/Library/CloudStorage/OneDrive-Persönlich/Studies/TeamprojektDataScience/resources/Kopfwelle_Z13/Kopfwelle_Serie_1/Messdaten/KW01.txt',sep = " ", header=None)
#kw01.colums = ["x-dim", "y-dim", "DWA"]
