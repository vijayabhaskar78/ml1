import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("medical_expenses.csv")
m = LinearRegression().fit(df[['age']], df['expenses'])
print("Prediction for age 40:", m.predict([[40]])[0])

"""
age,expenses
18,16884.92
19,1725.55
20,4449.46
21,21984.47
22,3866.86
23,3756.62
24,8240.59
25,7281.51
26,6406.41
27,28923.14
28,2721.32
29,27808.73
30,1826.84
31,44641.2


"""
