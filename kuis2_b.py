import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("E:\Program\Python\kuis-statistik\weatherHistory.csv")

temperature = dataframe['Temperature (C)']
plt.hist(temperature, bins=20, edgecolor='black')

plt.xlabel('Temperature (C)')
plt.ylabel('Frequency')
plt.title('Histogram of Temperature')
plt.show()
