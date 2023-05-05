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
