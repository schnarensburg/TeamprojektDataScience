import os.path

import pandas as pd

def generate_correlation_matrix(csv_file):
    print(csv_file)
    # Read CSV file into DataFrame
    data = pd.read_csv(csv_file)

    correlation_matrix = data.corr()
    correlation_matrix.to_csv('Correlate_Tooth.csv')
    return correlation_matrix

csv_file = 'newfile.csv'
matrix = generate_correlation_matrix(csv_file)
print(matrix)
