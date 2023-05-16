import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import requests
import csv

#Load data from csv file
cadZ13 = '/Users/aarongrommes/Library/CloudStorage/OneDrive-Persönlich/Studies/Semester 6/Teamprojekt/TeamprojektDataScience/TeamprojektDataScience/01_DATA/Z13/PointClouds/MeisterradZ13.xyz'
cadZ13URL = 'https://github.com/schnarensburg/TeamprojektDataScience/raw/4d3857cf1496cfa49c077d7b78cc36c0646cbd9b/00_GENERAL/visualisation/PointCloud%20to%203D%20Model/Z13_01.csv'

response = requests.get(cadZ13URL)
response.raise_for_status()
csv_data = response.text

csv_reader = csv.reader(csv_data.splitlines())


with open(csv_data, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    data = []
    for row in csv_reader:
        row_values = []
        for value in row:
            row_values.extend(map(float, value.split()))
        data.append(row_values)

#Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#Plot the gear data as a scatter plot
x, y, z = zip(*data)
ax.scatter(x, y, z, c=z, cmap='viridis')

#Set plot title and axis labels
ax.set_title('3D Model of a Gear')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

#show plot
plt.show()