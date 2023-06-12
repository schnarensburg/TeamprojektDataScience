import numpy as np
import statistics


def measure_variance(txt2D, Z19CAD):
    arithmetic_Mean = np.zeros(100)
    var = np.zeros(100)
    total_distances = np.zeros(19)
    for file, i in txt2D:
        total_distance = 0
        for tooth, i in range(1, 19):
            tooth_data = get_current_tooth_sample(i)
            tooth_CAD = get_current_tooth_CAD() # Inefficient, every tooth is calculated 100 times, maybe save them in a loop before
            total_distance += calculate_distance(tooth_data, tooth_CAD)
            total_distances[i] = total_distance

        arithmetic_Mean[i] = statistics.mean(total_distances)
        var[i] = statistics.variance(total_distances)



    arithmetic_Mean = statistics.mean(total_distances)
    var = statistics.variance(total_distances)



def calculate_distance(tooth_data, tooth_CAD):
    distances = np.zeros((tooth_data.shape[0], tooth_CAD.shape[0]))

    for i in range(tooth_data.shape[0]):
        for j in range(tooth_CAD.shape[0]):
            distances[i, j] = np.linalg.norm(tooth_data[i] - tooth_CAD[j])
    total_distance = int(np.sum(distances))
    return total_distance

def get_current_tooth_sample(i):

def get_current_tooth_CAD(i):

