import os.path
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import KFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor

in_dir = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(in_dir, '../08_Korrelation/newfile.csv')

data = pd.read_csv((folder_path))
X = data[['Mean', 'Variance', 'Max_Deviation', 'Min_Deviation']].values
Y = data[["fl' re", "fk' re", "fi' re", "fl' li", "fk' li", "fi' li"]].values

# Split data into training and testing sets
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled)

# Create separate models for each output value
models = []
for i in range(Y.shape[1]):
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(32, activation='relu', input_shape=(4,)))
    model.add(tf.keras.layers.Dense(64, activation='relu'))
    model.add(tf.keras.layers.Dense(1)) # Output Layer with 1 unit for every element in Y
    model.compile(loss='mean_squared_error', optimizer='adam')
    models.append(model)

# Define cross-validation strategy
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# Perform cross validation for each model
losses = []
for i, model in enumerate(models):
    print(f"Training and Evaluating Model {i+1}")
    cv_results = cross_val_score(model, X_scaled, Y[:, 1], cv=kfold, scoring='neg_mean_squared_error')
    loss = -cv_results.mean()
    losses.append(loss)
    print(f"Cross-Validation Results for Model {i+1}:")
    print(cv_results)
    print(f"Mean Squared Error for Model {i+1}: {loss}")

print("Overall Mean Squared Error: ", np.mean(losses))