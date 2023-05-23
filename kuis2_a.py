import pandas as pd
import scipy.stats as stats

data = pd.read_csv("E:\Program\Python\kuis-statistik\weatherHistory.csv")
temperature = data['Temperature (C)']

kstest_result = stats.kstest(temperature, 'norm')

alpha = 0.05
print("Nilai KS: ", kstest_result.statistic)

if kstest_result.pvalue < alpha:
    print("Atribut 'Temperature' tidak terdistribusi secara normal.")
else:
    print("Atribut 'Temperature' terdistribusi secara normal.")
