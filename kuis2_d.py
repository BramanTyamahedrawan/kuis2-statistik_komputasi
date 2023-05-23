import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv('weatherHistory.csv')
humidity = dataframe['Humidity']

plt.hist(humidity, bins=20, edgecolor='black')
plt.xlabel('Humidity')
plt.ylabel('Frequency')
plt.title('Histogram of Humidity')

plt.show()
