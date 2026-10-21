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

### 5. Conteneurisation avec Docker (Local)

```bash
# Construction de l'image
docker build -t house-price-api .

# Lancement du conteneur
docker run -d -p 8000:8000 --name api-container house-price-api
```

---

## 🌐 Déploiement sur la Machine Virtuelle Distante (Niveaux 0.5 & 2)

- **Hôte VM** : `40.66.48.24` (utilisateur : `ubuntu`)
- **Dossier de travail** : `/home/ubuntu/kn/TP_MLOPS`
- **Port exposé** : `8042`
- **Documentation Swagger en ligne** : [http://40.66.48.24:8042/docs](http://40.66.48.24:8042/docs)

### Commandes exécutées sur la VM :

```bash
# 1. Connexion SSH
ssh ubuntu@40.66.48.24

# 2. Création du répertoire et clonage du dépôt
mkdir -p /home/ubuntu/kn
cd /home/ubuntu/kn
git clone https://github.com/KahessLacessProduction/TP_MLOPS.git
cd TP_MLOPS

# 3. Build de l'image Docker
docker build -t kn-house-price-api .

# 4. Lancement du conteneur en arrière-plan
docker run -d -p 8042:8000 --name kn-house-price-api --restart unless-stopped kn-house-price-api
```

### Tester l'API distante :

Depuis n'importe quelle machine ou terminal :

```bash
# Test GET
curl http://40.66.48.24:8042/predict

# Test POST avec prédiction
curl -X POST http://40.66.48.24:8042/predict \
     -H "Content-Type: application/json" \
     -d '{"size": 100, "nb_rooms": 3, "garden": 1}'

# Ou via le script Python de test
python test_api.py http://40.66.48.24:8042
```

