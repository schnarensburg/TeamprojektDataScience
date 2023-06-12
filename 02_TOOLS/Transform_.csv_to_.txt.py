import csv
import os.path

dir_in = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(dir_in, '../01_DATA/Z13/PointClouds/2dimZ13CAD.csv')

dir_out = os.path.dirname(os.path.abspath(__file__))
txt_file = os.path.join(dir_out, '../01_DATA/Z13/PointClouds/2dimZ13CAD.txt')

with open(csv_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open(txt_file, 'w') as txt_file:
        for row in csv_reader:
            line = '\t'.join(row)

            txt_file.write(line + '\n')

print('Conversion complete')
