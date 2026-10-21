import streamlit as st
import joblib
import numpy as np

# Charger le modèle
model = joblib.load("regression.joblib")

# Titre de l'application
st.title("🏠 Prédiction du prix d'une maison")
st.write("Entrez les caractéristiques de la maison pour obtenir une estimation du prix.")

# Champs de formulaire
size = st.number_input("Taille (m²)", min_value=10, max_value=500, value=100, step=5)
nb_rooms = st.number_input("Nombre de chambres", min_value=1, max_value=10, value=3, step=1)
garden = st.number_input("Jardin (0 = Non, 1 = Oui)", min_value=0, max_value=1, value=0, step=1)

# Bouton de prédiction
if st.button("Prédire le prix"):
    # Préparer les données pour la prédiction
    features = np.array([[size, nb_rooms, garden]])
    prediction = model.predict(features)

    # Afficher le résultat
    st.write(f"### 💰 Prix estimé : {prediction[0]:,.2f} €")
