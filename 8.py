import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

df = pd.read_csv("heart.csv")
X = StandardScaler().fit_transform(df.select_dtypes(include='number'))

kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
gmm = GaussianMixture(n_components=2, random_state=0).fit(X)

kmeans_labels = kmeans.predict(X)
gmm_labels = gmm.predict(X)

print("KMeans Silhouette:", silhouette_score(X, kmeans_labels))
print("GMM Silhouette:", silhouette_score(X, gmm_labels))

