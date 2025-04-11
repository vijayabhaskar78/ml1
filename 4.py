import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("play_tennis.csv")
X = df.iloc[:, :-1].apply(LabelEncoder().fit_transform)
y = LabelEncoder().fit_transform(df.iloc[:, -1])

model = DecisionTreeClassifier(criterion="entropy").fit(X, y)
sample = pd.DataFrame([["Sunny","Cool","High","Strong"]], columns=X.columns)
sample = sample.apply(LabelEncoder().fit(df[X.columns]).transform)

print("Prediction:", df["PlayTennis"].unique()[model.predict(sample)[0]])

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
