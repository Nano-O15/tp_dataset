# OUKHEMANOU Mohand-Tahar
# Mastère DATA & IA
# TP Dataset
# [PRS] MIA 26.2

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

df = pd.read_csv("files/penguins.csv")

# Prétraitement des Données
df = df.drop("sex", axis='columns')

df = df.drop("year", axis='columns')

df = df.dropna()

df = df.reset_index(drop=True)

df = df.drop("Unnamed: 0", axis='columns')

# Création de mon axe des x
x = df[["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]]
print(x)

# Création de mon axe des y (avec l'espèce comme label)
y = df["species"].values
print(y)

# Liste des labels
print(df["species"].unique())

# Division du dataset pour l'entraînement
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Création de l'arbre de décision
# Profondeur maximum
max_depth = 4

# Initialisation et entraînement du classifieur
clf = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
clf.fit(X_train, Y_train)

# Prédictions
Y_pred = clf.predict(X_test)

# Précision (Accuracy) du Modèle
print("Accuracy:", accuracy_score(Y_test, Y_pred))

# Importance des caractéristiques
features_imp = clf.feature_importances_
for feature, importance in zip(["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"], features_imp):
    print(f"{feature}: {importance:.2f}")

# Visualisation de l'Arbre
plt.figure(figsize=(20, 10))
plot_tree(clf, feature_names=df.columns, class_names=df["species"].unique(), filled=True)
plt.show()
