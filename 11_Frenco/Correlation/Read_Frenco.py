import csv
from operator import itemgetter

def split_csv_file(input_file):
    # Define output filenames
    z13_frenco = 'z13_frenco.csv'
    z19_frenco = 'z19_frenco.csv'

    # Define columns not to copy
    columns_z13 = ['\ufeffVersuchsnummer', 'Z19']
    columns_z19 = ['\ufeffVersuchsnummer', 'Z13']

    # Open input
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    # Copy and sort rows
    sorted_z13 = sorted(rows, key=lambda x: int(x['Z13']))
    output_z13 = [{k: v for k, v in row.items() if k not in columns_z13} for row in sorted_z13]
    header_z13 = {k: k for k in rows[0].keys() if k not in columns_z13}
    sorted_z19 = sorted(rows, key=lambda x: int(x['Z19']))
    output_z19 = [{k: v for k, v in row.items() if k not in columns_z19} for row in sorted_z19]
    header_z19 = {k: k for k in rows[0].keys() if k not in columns_z19}
    print(header_z19)
    # Write copied and sorted rows to output files
    with open(z13_frenco, 'w', newline='') as file1:
        fieldnames = [column for column in reader.fieldnames if column not in columns_z13]
        writer1 = csv.DictWriter(file1, fieldnames=fieldnames)
        writer1.writeheader()
        writer1.writerows(output_z13)

    with open(z19_frenco, 'w', newline='') as file2:
        fieldnames = [column for column in reader.fieldnames if column not in columns_z19]
        writer2 = csv.DictWriter(file2, fieldnames=fieldnames)
        writer2.writeheader()
        writer2.writerows(output_z19)

    return z13_frenco, z19_frenco

split_csv_file('Datenauswertung-Frenco.csv')