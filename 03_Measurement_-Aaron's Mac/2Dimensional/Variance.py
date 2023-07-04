import math
import os
import numpy as np
import csv


def calculate_means(txt2D_folder, z13CAD):
    means_array = []
    file_list = os.listdir(txt2D_folder)

    for file in file_list:
        file_name = os.path.join(txt2D_folder, file)

        sum_mean = 0
        j = 0
        for tooth in range(1, 13):
            j += 1
            tooth_pc = get_current_tooth(file_name, j)
            tooth_CAD = get_current_tooth(z13CAD, j)
            for point1, point2 in zip(tooth_pc, tooth_CAD):
                x1, y1 = point1
                x2, y2 = point2
                sum_mean += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        mean = sum_mean / 13
        means_array.append([file, mean])

    print(f" Means: {means_array}")
    return means_array


def calculate_vars(txt2D_folder, z13CAD, means_array):
    vars_array = []
    file_list = os.listdir(txt2D_folder)

    for file in file_list:
        file_name = os.path.join(txt2D_folder, file)

        sum_var = 0
        j = 0
        for tooth in range(1, 13):
            j += 1
            tooth_pc = get_current_tooth(file_name, j)
            tooth_CAD = get_current_tooth(z13CAD, j)
            for point1, point2 in zip(tooth_pc, tooth_CAD):
                x1, y1 = point1
                x2, y2 = point2
                sum_var += (float(means_array[j][1]) - (math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))) ** 2
        variance = sum_var / 13
        vars_array.append([file, variance])

    print(f" Variances: {vars_array}")
    return vars_array

def get_current_tooth(file, j):
    corridor_angle = ((j+0.25) * 360/13, (j+1.25)*360/13)
    with open(file, 'r') as file:
        lines = file.readlines()

        # Extract X and Y for points within the area
        points = []

        for line in lines:
            x, y = map(float, line.split())
            angle = math.atan2(y, x)
            if angle < 0:
                angle += 2 * math.pi

            angle_degrees = math.degrees(angle)
            if corridor_angle[0] <= angle_degrees <= corridor_angle[1]:
                points.append([x, y])
    return np.array(points)

def sort_and_write_to_csv(means, variances, output_file_means, output_file_variances):
    means_sorted = sorted(means, key=lambda x: x[1], reverse=True)
    variances_sorted = sorted(variances, key=lambda x: x[1], reverse=True)

    with open(output_file_means, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Filename', 'Mean'])

        for mean in means_sorted:
            writer.writerow([mean[0], mean[1]])

    with open(output_file_variances, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Filename', 'Variance'])

        for var in variances_sorted:
            writer.writerow([var[0], var[1]])

txt2D_folder = '/Users/aarongrommes/Library/CloudStorage/OneDrive-Persönlich/Studies/Semester 6/Teamprojekt/TeamprojektDataScience/TeamprojektDataScience/01_DATA/Z13/PointClouds/.txt2D'
Z13CAD = '/Users/aarongrommes/Library/CloudStorage/OneDrive-Persönlich/Studies/Semester 6/Teamprojekt/TeamprojektDataScience/TeamprojektDataScience/01_DATA/Z13/PointClouds/2dimZ13CAD.txt'
means = calculate_means(txt2D_folder, Z13CAD)
variances = calculate_vars(txt2D_folder, Z13CAD, means)
output_file_means = '/Users/aarongrommes/Library/CloudStorage/OneDrive-Persönlich/Studies/Semester 6/Teamprojekt/TeamprojektDataScience/TeamprojektDataScience/10_RESULTS/2D_Analysis/means.csv'
output_file_variances = '/Users/aarongrommes/Library/CloudStorage/OneDrive-Persönlich/Studies/Semester 6/Teamprojekt/TeamprojektDataScience/TeamprojektDataScience/10_RESULTS/2D_Analysis/variances.csv'
sort_and_write_to_csv(means, variances, output_file_means, output_file_variances)