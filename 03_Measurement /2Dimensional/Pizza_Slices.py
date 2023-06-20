import math
import numpy as np
import matplotlib.pyplot as plt
import os

# Load the gear data from the txt
dir_in = os.path.dirname(__file__)
file_in = os.path.join(dir_in, '../../01_DATA/Z19/PointClouds/.txt2D/+01_2D.txt')
gear_data = np.loadtxt(os.path.join(dir_in, '../../01_DATA/Z19/PointClouds/2dimZ19CAD.txt'))

# Calculate the angle between each tooth slice
angle_per_slice = 360/19

# Create list to store separated teeth
teeth_slices = []


def is_point_in_circular_sector(point, radius, angle_range):
    px, py = point
    start_angle, end_angle = math.radians(angle_range[0]), math.radians(angle_range[1])

    # Calculate distance between point and center
    distance = math.sqrt((px) ** 2 + (py) ** 2)

    # Check if point is within circular sector's radius
    if distance <= radius:
        # Calculate angle between point and center
        angle = math.atan2(py, px)

        # Normalize angle between 0 and 2*pi
        if angle < 0:
            angle += 2 * math.pi
        # Check if angle is within sector
        if start_angle <= angle <= end_angle:
            return True
    return False

def save_points_within_corridor(gear_data, output_file, corridor_radius, corridor_angle):
    saved_points = []
    with open(gear_data, 'r') as file:
        lines = file.readlines()

        # Extract X and Y values for points within the area
        x_values = []
        y_values = []
        for line in lines:
            x, y = map(float, line.split())
            point = (x, y)

            if is_point_in_circular_sector(point, corridor_radius, corridor_angle):
                x_values.append(x)
                y_values.append(y)

        # Save the points within the area to the output file
        with open(output_file, 'w') as file:
            for x, y in zip(x_values, y_values):
                file.write(f"{x} {y}\n")

        # Plot the data points within the area
        plt.scatter(x_values, y_values, color='green', label='Points within Area')

        # Set labels and title
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Points within Circular Sector: +01_2D.txt')
        plt.legend()


plt.figure()
corridor_radius = 0.0035
corridor_angle = (0, 360/19)
save_points_within_corridor(file_in, 'new.txt', corridor_radius, corridor_angle)
plt.show()