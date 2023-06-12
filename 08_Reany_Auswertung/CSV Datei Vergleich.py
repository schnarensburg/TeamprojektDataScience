import os
import pandas as pd

# Pfad zum Ordner mit den CSV-Dateien angeben
folder_path = '/Users/moritz/PycharmProjects/TeamprojektDataScience/01_DATA/Z13/Reany Z13'

# Dictionary zur Speicherung der Zahlenwerte und Dateinamen erstellen
zahlenwerte = {}

# Alle Dateien im Ordner durchgehen
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        # Pfad zur aktuellen CSV-Datei erstellen
        file_path = os.path.join(folder_path, filename)

        # CSV-Datei in ein DataFrame laden und Trennzeichen angeben
        dataframe = pd.read_csv(file_path, encoding='latin-1')

        # Annahmen zum Spaltennamen und Zahlenwert treffen
        spaltenname = dataframe.columns[0]  # Name der Spalte, die den Wert enthält
        row_index = 34  # Index der gewünschten Zeile

        # Wert auslesen und zur Dictionary der Zahlenwerte hinzufügen
        zeile = dataframe.iloc[row_index]  # Ausgewählte Zeile
        wert = zeile[spaltenname]  # Wert in der Spalte
        zahlenwert = float(wert.split(';')[1])  # Zahlenwert befindet sich an zweiter Stelle
        zahlenwerte[filename] = zahlenwert

# Sortieren des Dictionaries nach den Zahlenwerten in aufsteigender Reihenfolge
sortierte_dateien = sorted(zahlenwerte.items(), key=lambda x: x[1])

# Ausgabe des Rankings
print("Ranking:")
for i, (datei, wert) in enumerate(sortierte_dateien):
    rang = i + 1
    print(f"Rang {rang}: Datei {datei} - Zahlenwert: {wert}")

# Konvertiere das Ranking in ein DataFrame
ranking_dataframe = pd.DataFrame(sortierte_dateien, columns=['Datei', 'Zahlenwert'])

# Speichere das Ranking in eine CSV-Datei
ranking_dataframe.to_csv('ranking.csv', index=False)