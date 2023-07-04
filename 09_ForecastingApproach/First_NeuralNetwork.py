import os.path
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


in_dir = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(in_dir, '../08_Korrelation/newfile.csv')

data = pd.read_csv(folder_path)
X = data[['Mean', 'Variance', 'Max_Deviation', 'Min_Deviation']].values
Y = data[["fl' re", "fk' re", "fi' re","fl' li", "fk' li", "fi' li"]].values

# Split data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Scale input features using StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scales = scaler.fit_transform(X_test)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(32, activation='relu', input_shape=(4,)))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(256, activation='relu'))
model.add(tf.keras.layers.Dense(6))  # Output layer with 4 units for the 4 output values

model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(X_train_scaled, Y_train, epochs=100, batch_size=64, verbose=1)

loss = model.evaluate(X_test, Y_test)
lossTrain = model.evaluate(X_train, Y_train)
print("Test loss:", loss)
print("Test lossTrain:", lossTrain)

# Assuming you have a new gear data point for which you want to make predictions
new_data = np.array([[1825.50563541552, 2532849157.24587, 7.42854435979431, 0.1875334973838]])  # Adjust the values according to your data

# Standardize the new data using the same scaler used for training data
new_data_scaled = scaler.transform(new_data)

# Make predictions for the new data
predictions = model.predict(new_data_scaled)
print("Predictions:", predictions)

