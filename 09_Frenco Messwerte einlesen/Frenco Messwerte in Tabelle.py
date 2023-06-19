import pandas as pd

# Excel-Datei laden
dataframe = pd.read_excel('/Users/moritz/PycharmProjects/TeamprojektDataScience/01_DATA/Frenco Messungen/Frenco Messungen Tabelle .xlsx', engine='openpyxl')

# Auf Spalten zugreifen
spalte1 = dataframe['Z13']
spalte2 = dataframe['Z19']

# Auf eine bestimmte Zeile zugreifen
zeile = dataframe.loc[2]

# Ausgabe der Werte
print(spalte1)
print(spalte2)
print(zeile)
