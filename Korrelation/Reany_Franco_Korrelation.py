import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import os
# CSV-Datei einlesen
df = pd.read_csv('/Users/aaronneumann/Documents/GitHub/TeamprojektDataScience/Korrelation/frenco-reany_korrelationsliste_,.csv')  # Setzen Sie hier den Pfad zu Ihrer Datei
independent_vars = df[["Fi_liZ13","Fi_liZ19","Fi_reZ13","Fi_reZ19"]].values
dependent_var = df[["Wälzfehler VW"]].values



#Skalierung der Variablen
scaler=StandardScaler()
x_scaled = scaler.fit_transform(independent_vars)
y_scaled = scaler.fit_transform(dependent_var)
# Multiple lineare Regression durchführen
model = LinearRegression().fit(x_scaled, y_scaled)

# Koeffizienten der Regression ausgeben
print('Intercept:', model.intercept_)
print('Coefficients:', model.coef_)

# Pearson-Korrelationen berechnen
correlations = df.corr(method='pearson')

print('Pearson correlation coefficients:')
print(correlations)
