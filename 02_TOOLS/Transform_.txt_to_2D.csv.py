import os
import csv

# Define input and output folder
dir_in = os.path.dirname(os.path.abspath(__file__))
input = os.path.join(dir_in, '../01_DATA/Z19/PointClouds/cutCADZ19.txt')

dir_out = os.path.dirname(os.path.abspath(__file__))
output = os.path.join(dir_out, '../01_DATA/Z19/PointClouds/2dimZ19CAD.csv')

def reduce_dimension(input, output):
        # Read the contents of the input file
    with open(input, 'r') as file:
        lines = file.readlines()
            # Remove first and last line and the y-coordinate
        points = [[float(x) for x in line.split()] for line in lines]
        points = remove_y(points)
        # Write points to a CSV
        with open(output, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(points)
    print('Reduction completed successfully')

def remove_y(points):
    return[[point[0], point[2]] for point in points]
reduce_dimension(input, output)

