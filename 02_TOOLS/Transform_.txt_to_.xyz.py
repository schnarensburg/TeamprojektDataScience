import os

script_in = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(script_in, '../01_DATA/Z19/PointClouds/.txt')

script_out = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(script_out, '../01_DATA/Z19/PointClouds/.xyz')

# Loop over all .txt files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        # Read the contents of the input file
        with open(os.path.join(input_folder, filename), 'r') as file:
            lines = file.readlines()

        # Remove the first and the last 2 rows
        selected_rows = lines[1:-1]

        # Convert the remaining rows into a list of 3D points
        point_cloud = [[float(x) for x in line.split()] for line in selected_rows]

        # Save the point cloud to the output file in .xyz format
        output_filename = os.path.splitext(filename)[0] + '.xyz'
        with open(os.path.join(output_folder, output_filename), 'w') as file:
            for point in point_cloud:
                file.write(f"{point[0]} {point[1]} {point[2]}\n")