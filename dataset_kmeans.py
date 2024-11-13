# OUKHEMANOU Mohand-Tahar
# Mastère DATA & IA
# TP Dataset
# [PRS] MIA 26.2

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

df = pd.read_csv("files/penguins.csv")

# Prétraitement des Données
df = df.drop("sex", axis='columns')

df = df.drop("year", axis='columns')

df = df.dropna()

df = df.reset_index(drop=True)

df = df.drop("Unnamed: 0", axis='columns')

data = df[["bill_length_mm", "bill_depth_mm",
           "flipper_length_mm", "body_mass_g"]]

data_norm = (data - data.mean()) / data.std()

# Calcul du SSE
sse = []
for i in range(1, 11):
    km = KMeans(n_clusters=i, init='random',
                n_init='auto', random_state=0)
    km.fit_predict(data_norm)
    sse.append(km.inertia_)

# Affichage du Graph
plt.plot(range(1, 11), sse, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

# Calcul du Silhouette Score
score = []
for i in range(2, 11):
    km = KMeans(n_clusters=i, init='random',
                n_init='auto', random_state=0)
    km.fit_predict(data_norm)
    sil_score = silhouette_score(data_norm, km.labels_)
    score.append(sil_score)

# Affichage du Graph
plt.plot(range(2, 11), score, marker='o')
plt.title('Clustering Quality')
plt.xlabel('Number of Clusters')
plt.ylabel('Slhouette Score')
plt.show()

# K-Means Clustering (avec en exemple les longueur et profondeur de bec)
km = KMeans(n_clusters=3, init='random',
            n_init='auto', random_state=0)
km.fit_predict(data_norm)
df['cluster'] = km.labels_

print(df)

# Affichage des Graphs
sns.scatterplot(x="bill_length_mm", y="bill_depth_mm",
                hue="species", palette="flare", data=df)
plt.xlabel("Bill Length (mm)")
plt.ylabel("Bill Depth (mm)")
plt.title("Penguins Species Distribution")
plt.show()

sns.scatterplot(x="bill_length_mm", y="bill_depth_mm",
                hue="island", palette="flare", data=df)
plt.xlabel("Bill Length (mm)")
plt.ylabel("Bill Depth (mm)")
plt.title("Penguins Island Distribution")
plt.show()

sns.scatterplot(x="bill_length_mm", y="bill_depth_mm",
                hue="cluster", palette="flare", data=df)
plt.xlabel("Bill Length (mm)")
plt.ylabel("Bill Depth (mm)")
plt.title("K-Means Clustering")
plt.show()
