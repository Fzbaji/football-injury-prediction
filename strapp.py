import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Charger le modèle pré-entraîné
model = joblib.load(r'C:\Users\Dell\Desktop\Projet_IA\modele4_tab.h5')

# Titre de l'application
#st.title("Prédiction des Blessures Musculaires")

## Interface utilisateur
st.title("Prédiction du Risque de Blessure des Joueurs de Football")
st.header("Entrez les informations du joueur")

# Formulaire pour entrer les données utilisateur
st.sidebar.header("Paramètres d'entrée")
minutes_jouees = st.sidebar.number_input("Minutes jouées", min_value=0, step=1, value=1000)
fatigue = st.sidebar.slider("Fatigue (%)", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
heures_entrainement = st.sidebar.number_input("Heures d’entraînement", min_value=0, step=1, value=20)
age = st.sidebar.number_input("Âge", min_value=0, step=1, value=25)
historique_blessures = st.sidebar.selectbox("Historique de blessures musculaires", [0, 1])
contact_sans_contact = st.sidebar.selectbox("Sans contact physique ?", ["Oui", "Non"])

# Conversion du champ 'Sans contact physique ?' en binaire
contact_physique_encoded = 1 if contact_sans_contact == "Oui" else 0

# Préparer les données sous forme de dataframe
data_input = pd.DataFrame({
    "Minutes jouées": [minutes_jouees],
    "Fatigue (%)": [fatigue],
    "Heures d’entraînement": [heures_entrainement],
    "Âge": [age],
    "Historique de blessures musculaires": [historique_blessures],
    "Contact physique_Sans contact": [bool(contact_physique_encoded)]
})

st.write("### Données entrées :")
st.write(data_input)

# Fonction pour prédire avec scaling
def predire_risque_blessure(data):
    try:
        prediction = model.predict(data)
        probabilities = model.predict_proba(data)
        return prediction, probabilities
    except ValueError as e:
        st.write(f"Erreur dans la prédiction : {e}")
        return None, None
    

# Prédiction
if st.button("Prédire le risque de blessure"):
    prediction, probabilities = predire_risque_blessure(data_input)
    if prediction is not None:
        st.write(f"Prédiction brute : {prediction[0]}")
        st.write(f"Probabilité de blessure : {probabilities[0][1]:.2f}")
        st.write(f"Probabilité de pas de blessure : {probabilities[0][0]:.2f}")

        if prediction[0] == 1:
            st.error("Le joueur est à risque de blessure.")
        else:
            st.success("Le joueur ne présente pas de risque immédiat de blessure.")
    else:
        st.write("Une erreur s'est produite lors de la prédiction.")