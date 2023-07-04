import pandas as pd
import csv

def generate_new_csv(xlsx_file, csv_file):
    # Read xlsx file
    data = pd.read_excel(xlsx_file)
    selected_columns = data.columns[2:]
    selected_data = data[selected_columns]
    selected_data.to_csv(csv_file, index=False)


xlsx_file = '/Users/aarongrommes/Library/CloudStorage/OneDrive-Persönlich/Studies/Semester 6/Teamprojekt/TeamprojektDataScience/TeamprojektDataScience/01_DATA/Z19/Z19 Datensammlung.xlsx'
csv_file = 'Z19_Results.csv'

generate_new_csv(xlsx_file, csv_file)


