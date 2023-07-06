import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# File paths for input and output
data_folder = 'C:/Users/siewe/TeamprojektDataScience/Daten/'
df1_input = os.path.join(data_folder, 'Datenauswertung-Frenco.csv')
df2_input = os.path.join(data_folder, 'Z13-Datensammlung.csv')
df3_input = os.path.join(data_folder, 'Z19 Datensammlung.csv')
output_folder = os.path.join(data_folder, 'Output')
os.makedirs(output_folder, exist_ok=True)

# Read Excel files and drop empty cells
df1 = pd.read_csv(df1_input).dropna()
df2 = pd.read_csv(df2_input).dropna()
df3 = pd.read_csv(df3_input).dropna()

# Columns from Frenco data analysis Excel
wf_vw = df1['Wälzfehler VW']
wf_rw = df1['Wälzfehler RW']
ws_vw = df1['Wälzsprung VW']
ws_rw = df1['Wälzsprung RW']

# Merge selected columns from Frenco data analysis with Z13 and Z19 data
merged_df1 = pd.merge(df1, df2, how='inner', on='Z13')
merged_df2 = pd.merge(df1, df3, how='inner', on='Z19')

# Extract parameters from merged DataFrames
parameters1 = ['Fi li', 'Fi re', 'fl li', 'fl re', 'fk li', 'fk re', 'fi li', 'fi re']
parameters2 = ['Fi li', 'Fi re', 'fl li', 'fl re', 'fk li', 'fk re', 'fi li', 'fi re']
params_df1 = merged_df1[parameters1]
params_df2 = merged_df2[parameters2]

# Create matrices with arrays as individual fields
m1 = np.vstack((wf_vw, wf_rw, ws_vw, ws_rw, params_df1.values.T))
m2 = np.vstack((wf_vw, wf_rw, ws_vw, ws_rw, params_df2.values.T))

# Compute correlation matrices
correlation_matrix1 = np.corrcoef(m1)
correlation_matrix2 = np.corrcoef(m2)

# Create DataFrames for the correlation matrices
df4 = pd.DataFrame(correlation_matrix1)
df5 = pd.DataFrame(correlation_matrix2)

# File paths for saving
output_path1 = os.path.join(output_folder, 'Z13CorrelationMatrix.xlsx')
output_path2 = os.path.join(output_folder, 'Z19CorrelationMatrix.xlsx')

# Save correlation matrices as Excel files
df4.to_excel(output_path1, index=False)
df5.to_excel(output_path2, index=False)

# Print correlation matrices
print(correlation_matrix1)
print(correlation_matrix2)

# Plot a heatmap of correlation_matrix1
plt.imshow(correlation_matrix1, cmap='RdYlBu', vmin=-1, vmax=1)

# Set axis labels
labels = ['WF vw', 'WF rw', 'WS vw', 'WS rw'] + parameters1
plt.xticks(range(len(labels)), labels)
plt.yticks(range(len(labels)), labels)

# Add colorbar
cbar = plt.colorbar()
cbar.set_label('Correlation Coefficient')

# Set title and adjust layout
plt.title('Correlation Matrix')
plt.tight_layout()

# Show the plot
plt.show()
