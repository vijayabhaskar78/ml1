from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X, y = load_iris(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y)
m = KNeighborsClassifier().fit(X_tr, y_tr)
p = m.predict(X_te)

print("✅ Correct:")
[print(f"P:{i} A:{j}") for i,j in zip(p,y_te) if i==j]

print("❌ Wrong:")
[print(f"P:{i} A:{j}") for i,j in zip(p,y_te) if i!=j]
