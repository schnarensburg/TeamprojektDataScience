import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

#Einlesen der Excel Dateien und Löschen von leeren Zellen
df1_input = 'C:/Users/siewe/TeamprojektDataScience/Daten/Datenauswertung-Frenco.csv'
df1 = pd.read_csv(df1_input)
df1 = df1.dropna()

df2_input = 'C:/Users/siewe/TeamprojektDataScience/Daten/Z13-Datensammlung.csv'
df2 = pd.read_csv(df2_input)
df2 = df2.dropna()

df3_input = 'C:/Users/siewe/TeamprojektDataScience/Daten/Z19 Datensammlung.csv'
df3 = pd.read_csv(df3_input)
df3 = df3.dropna()

#Speichern der Spalten aus der Frenco-Datenauswertung Excel
wf_vw = df1['Wälzfehler VW']
wf_rw = df1['Wälzfehler RW']
ws_vw = df1['Wälzsprung VW']
ws_rw = df1['Wälzsprung RW']

#Auswahl der Zellenwerte die in der Frenco Datenauswertung erfasst worden sind
merged_df1 = pd.merge(df1, df2, how='inner', on='Z13')
merged_df2 = pd.merge(df1, df3, how='inner', on='Z19')

#concatenated = pd.concat([df1, df3], axis=0, join='inner', keys=['df1', 'df3'])


#Speicherung der jeweiligen Parameter in Variablen aus Z13 Datensammlung
Fi_li1 = merged_df1['Fi li'].tolist()
Fi_re1 = merged_df1['Fi re'].tolist()
fl_li1 = merged_df1['fl li'].tolist()
fl_re1 = merged_df1['fl re'].tolist()
fk_li1 = merged_df1['fk li'].tolist()
fk_re1 = merged_df1['fk re'].tolist()
fi_li1 = merged_df1['fi li'].tolist()
fi_re1 = merged_df1['fi re'].tolist()

#Speicherung der jeweiligen Parameter in Variablen aus Z19 Datensammlung
Fi_li2 = merged_df2['Fi li'].tolist()
Fi_re2 = merged_df2['Fi re'].tolist()
fl_li2 = merged_df2['fl li'].tolist()
fl_re2 = merged_df2['fl re'].tolist()
fk_li2 = merged_df2['fk li'].tolist()
fk_re2 = merged_df2['fk re'].tolist()
fi_li2 = merged_df2['fi li'].tolist()
fi_re2 = merged_df2['fi re'].tolist()

#Bilden der Matrizen mit Arrays als einzelnen Feldern
m1 = np.vstack((wf_vw, wf_rw, ws_vw, ws_rw, Fi_li1, Fi_re1, fl_li1, fl_re1, fk_li1, fk_re1, fi_li1, fi_re1))
m2 = np.vstack((wf_vw, wf_rw, ws_vw, ws_rw, Fi_li2, Fi_re2, fl_li2, fl_re2, fk_li2, fk_re2, fi_li2, fi_re2))


#Bilden der Korrelationsmatrizen
correlation_matrix1 = np.corrcoef(m1)
correlation_matrix2 = np.corrcoef(m2)

#Erstellen von Data Frames für die erzeugten Korrelationsmatrizen
df4 = pd.DataFrame(correlation_matrix1)
df5 = pd.DataFrame(correlation_matrix2)

#Bennenung der Pfade für Speicherung
dataname1 = 'C:/Users/siewe/TeamprojektDataScience/Daten/Z13Korrelationsmatrix.xlsx'
dataname2 = 'C:/Users/siewe/TeamprojektDataScience/Daten/Z19Korrelationsmatrix.xlsx'

#Speicherung in Excel Sheets
df4.to_excel(dataname1, index=False)
df5.to_excel(dataname2, index=False)

#Ausgabe beliebiger vorab definierter Korrelationsmatrix
print(correlation_matrix1)
print(correlation_matrix2)

#Grafische Visualisierung der Messergebnisse einer Korrelationsmatrix
#Grafik erstellen
plt.imshow(correlation_matrix1, cmap='RdYlBu', vmin=-1, vmax=1)

# Achsenbeschriftung festlegen
labels = ['WF vw', 'WF rw', 'WS vw', 'WS rw', 'Fi_li', 'Fi_re', 'fl_li', 'fl_re', 'fk_li', 'fk_re', 'fi_li', 'fi_re']
plt.xticks(range(len(labels)), labels)
plt.yticks(range(len(labels)), labels)

# Farb-Legende hinzufügen
cbar = plt.colorbar()
cbar.set_label('Korrelationskoeffizient')

# Titel und Anpassung der Layouts
plt.title('Korrelationsmatrix')
plt.tight_layout()

# Grafik anzeigen
plt.show()
