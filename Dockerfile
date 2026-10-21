FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les dépendances et les installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source et le modèle
COPY api.py .
COPY regression.joblib .

# Exposer le port
EXPOSE 8000

# Lancer le serveur
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
