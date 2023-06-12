import pandas as pd

# CSV-Dateien laden
ranking1 = pd.read_csv('/Users/moritz/PycharmProjects/TeamprojektDataScience/08_Reany_Auswertung/Ranking Frenco Messungen/Auswertung')
ranking2 = pd.read_csv('/Users/moritz/PycharmProjects/TeamprojektDataScience/08_Reany_Auswertung/ranking.csv')

# Spaltennamen festlegen
spalte_name1 = 'Wälzfehler vw '  # Ersetze 'Spalte1' durch den Namen der Spalte im Ranking 1
spalte_name2 = 'Zahlenwert'  # Ersetze 'Spalte2' durch den Namen der Spalte im Ranking 2

# Auf die erforderlichen Spalten zugreifen
spalte1 = ranking1[spalte_name1]
spalte2 = ranking2[spalte_name2]

# Korrelation berechnen
korrelation = spalte1.corr(spalte2)

# Ausgabe der Korrelation
print(f"Korrelation: {korrelation}")
