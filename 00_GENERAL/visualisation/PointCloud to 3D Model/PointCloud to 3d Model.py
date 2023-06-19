import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
meisterradZ13 = '/Users/aarongrommes/Library/CloudStorage/OneDrive-Persönlich/Studies/Semester 6/Teamprojekt/TeamprojektDataScience/TeamprojektDataScience/01_DATA/Z13/PointClouds/MeiterradCutZ13.xyz'
kw01Z13 = '/Users/aarongrommes/Library/CloudStorage/OneDrive-Persönlich/Studies/Semester 6/Teamprojekt/TeamprojektDataScience/TeamprojektDataScience/00_GENERAL/resources/Kopfwelle_Z13/Transformed data/xyzFormat/KW01.xyz'

#Load data from csv/xyz file
with open(meisterradZ13, 'r') as csv_file:
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