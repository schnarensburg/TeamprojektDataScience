import pandas
import pandas as pd
from scipy.stats import pearsonr, spearmanr, kendalltau

def calculate_correlations(csv_file):
    # Load CSV
    df = pd.read_csv(csv_file)
    columns = df.columns

    # Calculate correlation coefficients for each pair of columns
    correlations = []

    for i in range(len(columns)):
        for j in range(i+1, len(columns)):
            var1 = df[columns[i]]
            var2 = df[columns[j]]

            # Calculate Pearson
            pearson_corr, _ = pearsonr(var1, var2)
            # Calculate Spearman
            spearman_corr, _ = spearmanr(var1, var2)
            # Calculate Kendall
            kendall_corr, _ = kendalltau(var1, var2)

            correlations.append((columns[i], columns[j], pearson_corr, spearman_corr, kendall_corr))

    # Create DataFrame to store correlations
    correlations_df = pd.DataFrame(correlations, columns=['Variable 1', 'Variable 2', 'Pearson', 'Spearman', 'Kendall'])

    filtered_corr = correlations_df[(correlations_df['Pearson'] > 0.1) |
                                               (correlations_df['Spearman'] > 0.1) |
                                               (correlations_df['Kendall'] > 0.1)]

    return filtered_corr

print(calculate_correlations('Z19_Results.csv'))