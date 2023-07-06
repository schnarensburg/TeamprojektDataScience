import csv
from operator import itemgetter

def split_csv_file(input_file):
    # Define output filenames
    z13_frenco = 'z13_frenco.csv'
    z19_frenco = 'z19_frenco.csv'

    # Define columns to copy
    columns_z13 = ['Z13', 'Wälzfehler VW', 'Wälzfehler RW', 'Wälzsprung VW', 'Wälzsprung RW']
    columns_z19 = ['Z13', 'Wälzfehler VW', 'Wälzfehler RW', 'Wälzsprung VW', 'Wälzsprung RW']

    # Open input
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Copy and sort rows
    output_z13 = sorted((row for row in rows), key=itemgetter('Z13'))
    output_z19 = sorted((row for row in rows), key=itemgetter('Z19'))

    # Write copied and sorted rows to output files
    with open(z13_frenco, 'w', newline='') as file1:
        writer1 = csv.writer(file1)
        writer1.writeheader()
        writer1.writerows(output_z13)

    with open(z19_frenco, 'w', newline='') as file2:
        writer2 = csv.writer(file2)
        writer2.writeheader()
        writer2.writerows(output_z19)

    return z13_frenco, z19_frenco

split_csv_file()