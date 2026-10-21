# TP MLOps - Déploiement d'un modèle de Machine Learning

Ce projet implémente le cycle de déploiement d'un modèle de Machine Learning (régression linéaire pour l'estimation de prix immobiliers) à travers plusieurs étapes :
1. **Application interactive avec Streamlit**
2. **Service web RESTful avec FastAPI**
3. **Conteneurisation avec Docker**

---

## 📁 Structure du projet

- `train_model.py` : Script d'entraînement du modèle de régression linéaire à partir de `houses.csv` et sauvegarde dans `regression.joblib`.
- `houses.csv` : Jeu de données d'entraînement (caractéristiques des maisons et prix).
- `regression.joblib` : Modèle de régression sérialisé.
- `model_app.py` : Interface utilisateur Streamlit pour tester les prédictions en direct.
- `api.py` : API FastAPI exposant l'endpoint `/predict` (GET pour test initial et POST pour prédiction avec payload JSON).
- `test_api.py` : Script de test automatisé des endpoints FastAPI avec la bibliothèque `requests`.
- `Dockerfile` : Définition de l'image Docker pour packager et déployer l'API FastAPI.
- `.dockerignore` : Fichiers exclus du build de l'image Docker.
- `requirements.txt` : Dépendances Python du projet.

---

## 🚀 Guide d'utilisation

### 1. Installation des dépendances

```bash
pip install -r requirements.txt
```

### 2. Entraînement du modèle

```bash
python train_model.py
```

### 3. Lancement de l'interface Streamlit

```bash
streamlit run model_app.py
```

### 4. Lancement et test de l'API FastAPI

```bash
# Lancement de l'API
uvicorn api:app --reload --port 8000

# Dans un autre terminal : tests des endpoints
python test_api.py
```

Documentation interactive Swagger disponible sur : `http://localhost:8000/docs`.

### 5. Conteneurisation avec Docker

```bash
# Construction de l'image
docker build -t house-price-api .

# Lancement du conteneur
docker run -d -p 8000:8000 --name api-container house-price-api
```
