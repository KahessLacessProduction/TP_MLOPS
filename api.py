from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Créer l'application FastAPI
app = FastAPI(title="House Price Prediction API")

# Charger le modèle au démarrage
model = joblib.load("regression.joblib")


# Schéma de données pour la requête POST
class HouseFeatures(BaseModel):
    size: float
    nb_rooms: int
    garden: int


# Niveau 0 — Préambule : GET /predict retourne une valeur fixe
@app.get("/predict")
def predict_get():
    return {"y_pred": 2}


# Niveau 0 — POST /predict avec le modèle de prédiction
@app.post("/predict")
def predict_post(features: HouseFeatures):
    # Préparer les données
    X = np.array([[features.size, features.nb_rooms, features.garden]])

    # Faire la prédiction
    prediction = model.predict(X)

    return {"y_pred": round(prediction[0], 2)}
