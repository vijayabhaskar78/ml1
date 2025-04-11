import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

X = pd.read_csv('sample_dataset.csv')
x, y = X.iloc[:, :-1], X.iloc[:, -1]
xtr, xt, ytr, yt = train_test_split(x, y, test_size=0.2)
m = GaussianNB().fit(xtr, ytr)
yp = m.predict(xt)
print("Acc:", accuracy_score(yt, yp)*100)


"""
Dataset:
Outlook,Temperature,Humidity,Windy,PlayTennis
Sunny,Hot,High,False,No
Sunny,Hot,High,True,No
Overcast,Hot,High,False,Yes
Rain,Mild,High,False,Yes
Rain,Cool,Normal,False,Yes
Rain,Cool,Normal,True,No
Overcast,Cool,Normal,True,Yes
Sunny,Mild,High,False,No
Sunny,Cool,Normal,False,Yes
Rain,Mild,Normal,False,Yes
Sunny,Mild,Normal,True,Yes
Overcast,Mild,High,True,Yes
Overcast,Hot,Normal,False,Yes
Rain,Mild,High,True,No
"""
