import csv

csv_file = '../01_DATA/Z19/PointClouds/2dimZ19CAD.csv'
txt_file = '../01_DATA/Z19/PointClouds/2dimZ19CAD.txt'

with open(csv_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open(txt_file, 'w') as txt_file:
        for row in csv_reader:
            line = '\t'.join(row)

            txt_file.write(line + '\n')

print('Conversion complete')
