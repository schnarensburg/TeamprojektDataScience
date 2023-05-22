import pandas as pd
import matplotlib.pyplot as plt
import os

#Load MeisterradCutZ19
script_dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(script_dir, "../02_TOOLS/2dimCAD.csv")
df = pd.read_csv(file, header=None)

x = df.iloc[:, 0]
y = df.iloc[:, 1]

plt.scatter(x, y)
plt.xlabel('X-asis')
plt.ylabel('Y-asis')
plt.title('2D Coordinate Plot')
plt.show()


