import os

input_folder = '/Users/aaronneumann/Documents/GitHub/TeamprojektDataScience/01_DATA/Z19/Test File'  # replace with the path to your input folder
output_folder = '/Users/aaronneumann/Documents/GitHub/TeamprojektDataScience/01_DATA/Z19/PointClouds/Output_Test'  # replace with the path to your output folder

# Loop over all .txt files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        # Read the contents of the input file
        with open(os.path.join(input_folder, filename), 'r') as file:
            lines = file.readlines()

        # Remove the first and the last 2 rows
        selected_rows = lines[2:-2]

        # Convert the remaining rows into a list of 3D points
        point_cloud = [[float(x) for x in line.split()] for line in selected_rows]

        # Save the point cloud to the output file in .xyz format
        output_filename = os.path.splitext(filename)[0] + '.xyz'
        with open(os.path.join(output_folder, output_filename), 'w') as file:
            for point in point_cloud:
                file.write(f"{point[0]} {point[1]} {point[2]}\n")