import pandas as pd

# Pfad zur CSV-Datei angeben
file_path = '/Users/moritz/PycharmProjects/TeamprojektDataScience/01_DATA/Z13/Reany Z13/2022_2_22_KW_001.txt.csv'

# CSV-Datei in ein DataFrame laden und Trennzeichen angeben
dataframe = pd.read_csv(file_path, encoding='latin-1')



row_index = 34  # Index der gewünschten Zeile
spaltenname = 'sep=;'  # Name der Spalte, die den Wert enthält

zeile = dataframe.iloc[row_index]  # Ausgewählte Zeile
werte = zeile[spaltenname].split(';')  # Werte in der Spalte aufteilen
zahlenwert = float(werte[1])  # Zahlenwert befindet sich an zweiter Stelle

print(zahlenwert)

