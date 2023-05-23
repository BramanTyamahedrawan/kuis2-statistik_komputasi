import pandas as pd
from scipy import stats

dataframe = pd.read_csv('E:\Program\Python\kuis-statistik\weatherHistory.csv')
humidity = dataframe['Humidity']
kstest_result = stats.kstest(humidity, 'norm')

alpha = 0.01
print("Nilai KS:", kstest_result.statistic)

if kstest_result.pvalue < alpha:
    print("Atribut 'Humidity' tidak terdistribusi secara normal.")
else:
    print("Atribut 'Humidity' terdistribusi secara normal.")
