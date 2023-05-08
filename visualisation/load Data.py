import numpy as np
import open3d as o3d
import requests
import csv

url = 'https://raw.githubusercontent.com/schnarensburg/TeamprojektDataScience/main/resources/Kopfwelle_Z13/Kopfwelle_Serie_1/Messdaten/KW01.txt'
response = requests.get(url)

if response.status_code == 200:
    file_contents = response.content.decode("utf-8")

    with open('daten01.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        for line in file_contents.split('\n'):
            line = line.split(',')
            writer.writerow(line)
else:
    print("Error: could not retrieve file from github")

with open ('daten01.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    lines = list(csv_reader)
    lines = lines[1:-1]
with open ('PointCloud to 3D Model/Z13_01.csv', 'w', newline='') as new_csv_file:
    csv_writer = csv.writer(new_csv_file)
    csv_writer.writerows(lines)


def print_CSV(file):
    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = [row for row in csv_reader]
        for row in rows:
            row = [element.rstrip() for element in row]
            print(row)


print_CSV('PointCloud to 3D Model/Z13_01.csv')