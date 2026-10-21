import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Charger les données
df = pd.read_csv("houses.csv")

# Séparer les features et la cible
X = df[["size", "nb_rooms", "garden"]]
y = df["price"]

# Entraîner le modèle
model = LinearRegression()
model.fit(X, y)

# Sauvegarder le modèle
joblib.dump(model, "regression.joblib")

print("Modèle entraîné et sauvegardé dans regression.joblib")
print(f"Score R² : {model.score(X, y):.4f}")
print(f"Coefficients : size={model.coef_[0]:.2f}, nb_rooms={model.coef_[1]:.2f}, garden={model.coef_[2]:.2f}")
print(f"Intercept : {model.intercept_:.2f}")
