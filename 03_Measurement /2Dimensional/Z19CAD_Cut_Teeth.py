import os.path
import matplotlib.pyplot as plt
import numpy as np
import math

def calculate_center(coordinates):
    x_sum = 0
    y_sum = 0
    num_points = len(coordinates)

    for x,y in coordinates:
        x_sum += x
        y_sum += y

    center_x = x_sum / num_points
    center_y = y_sum / num_points

    return center_x, center_y

def read_coodrinates_from_file(file_path):
    coordinates = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split())
            coordinates.append((x, y))
    return coordinates

def filter_points_by_radius(point_cloud, inner_radius, center, output_file):
    with open(output_file, 'w') as file:
        for point in point_cloud:
            distance = ((center[0] - point[0])**2 + (center[1] - point[1])**2)**0.5
            if inner_radius <= distance:
                file.write(f"{point[0]} {point[1]}\n")

    return output_file

def separate_teeth(coordinates, center_x, center_y, num_teeth):
    num_points = len(coordinates)
    tooth_points = [[] for _ in range(num_teeth)]
    angles_per_tooth = 360 / num_teeth

    for point in coordinates:
        x, y = point
        dx = x - center_x
        dy = y - center_y
        angle = math.degrees(math.atan2(dx, dy))
        tooth_index = int((angle + 180) // angles_per_tooth)
        tooth_points[tooth_index].append(point)
        print('angle: ' + str(angle) + ' -- tooth_index: ' + str(tooth_index))

    tooth_arrays = [np.array(points) for points in tooth_points]
    return tooth_arrays

def visualize_tooth(tooth_array):
    x = tooth_array[:, 0]
    y = tooth_array[:, 1]

    plt.scatter(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Visualization of a Single Tooth')
    plt.grid(True)
    plt.show()

def main():
    dir = os.path.dirname(__file__)
    file_path = os.path.join(dir, '../../01_DATA/Z19/PointClouds/2dimZ19CAD.txt')

    coordinates = read_coodrinates_from_file(file_path)
    center_x, center_y = calculate_center(coordinates)
    print("Center coordinates: ({:.2f}, {:.2f})".format(center_x, center_y))
    coordinates_filtered = 'filteredZ19CAD.txt'# filter_points_by_radius(coordinates, 3.5, (center_x, center_y))
    num_teeth = 19
    tooth_arrays = separate_teeth(coordinates_filtered, center_x, center_y, num_teeth)

    visualize_tooth(tooth_arrays[0])
    '''
    for i, tooth_array in enumerate(tooth_arrays):
        print("Tooth {}: {}".format(i+1, tooth_array))
    '''

if __name__ == '__main__':
    main()
