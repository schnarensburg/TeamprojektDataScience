import math
import os


def read_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = line.strip().split()
            data.append((float(x), float(y)))
    return data


def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def calculate_distance(file1, file2):
    data1 = read_data(file1)
    data2 = read_data(file2)

    distance = 0
    for point1, point2 in zip(data1, data2):
        distance += euclidean_distance(point1, point2)

    return distance

def calculate_distances_for_folder(folder_path, file1_path):
    file_list = os.listdir(folder_path)
    for file_name in file_list:
        file2_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file2_path):
            distance = calculate_distance(file1_path, file2_path)
            print(f"distance between 2dimZ13CAD and {file_name} is: {distance}")

# Provide the paths to the two text files
dir_in = os.path.dirname(os.path.abspath(__file__))
file1_path = os.path.join(dir_in, '../../01_DATA/Z13/PointClouds/2dimZ13CAD.txt')
file2_path = os.path.join(dir_in, '../../01_DATA/Z13/PointClouds/.txt2D')

distance = calculate_distances_for_folder(file2_path, file1_path)