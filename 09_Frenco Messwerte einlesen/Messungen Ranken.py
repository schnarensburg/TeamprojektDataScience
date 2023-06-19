import pandas as pd

# Excel-Datei laden
dataframe = pd.read_excel('/Users/moritz/PycharmProjects/TeamprojektDataScience/01_DATA/Frenco Messungen/Frenco Messungen sortiert.xlsx', engine='openpyxl')

# Spaltennamen festlegen
spalte_name1 = 'Wälzfehler vw '  # Ersetze 'Spaltenname1' durch den Namen der Spalte für das Ranking
spalte_name2 = 'Z13'  # Ersetze 'Spaltenname2' durch den Namen der Spalte mit den zugehörigen Werten

# Auf die erforderlichen Spalten zugreifen
spalte1 = dataframe[spalte_name1]
spalte2 = dataframe[spalte_name2]

# Sortiere die Werte in aufsteigender Reihenfolge und erstelle das Ranking
sortierte_spalte1 = spalte1.sort_values(ascending=True)
ranking = pd.Series(range(1, len(sortierte_spalte1) + 1), index=sortierte_spalte1.index)

# Verknüpfe das Ranking mit den Werten aus der zweiten Spalte
ergebnis = pd.concat([ranking, spalte1, spalte2], axis=1)

# Ausgabe der Ergebnisse
print(ergebnis)


