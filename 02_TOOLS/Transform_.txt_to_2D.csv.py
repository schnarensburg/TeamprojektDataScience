import os
import csv

# Define input and output folder
dir_in = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(dir_in, '../01_DATA/Z19/PointClouds/.txt')

dir_out = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(dir_out, '../01_DATA/Z19/PointClouds/.csv2D')

def reduce_dimension(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            # Read the contents of the input file
            with open(os.path.join(input_folder, filename), 'r') as file:
                lines = file.readlines()

            # Remove first and last line and the y-coordinate
            selected_lines = lines[1:-1]
            points = [[float(x) for x in line.split()] for line in selected_lines]
            points = remove_y(points)

            output_filename = os.path.splitext(filename)[0] + '_2D.csv'
            output_path = os.path.join(output_folder, output_filename)

            # Write points to a CSV
            with open(output_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(points)
    print('Reduction completed successfully')

def remove_y(points):
    return[[point[0], point[1]] for point in points]
reduce_dimension(input_folder, output_folder)

