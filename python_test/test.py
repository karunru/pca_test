import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("test_data.csv",header=None)

print(df)

height = df[0]
weight = df[1]

plt.plot(height,weight,"o")
plt.show()

avex = np.average(height)
avey = np.average(weight)

print(avex)
print(avey)
