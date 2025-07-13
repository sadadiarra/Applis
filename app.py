import streamlit as st
import pandas as pd
import numpy as np
from joblib import load

# Charger le modèle
model = load("random_forest_model.joblib")

st.set_page_config(page_title="Prédiction Prix Laptop", layout="centered")

st.title("💻 Prédiction du Prix d’un Laptop")

# Interface utilisateur
company = st.selectbox("Marque", ['Apple', 'Asus', 'Dell', 'HP', 'Lenovo', 'MSI', 'Other'])
typename = st.selectbox("Type", ['Ultrabook', 'Notebook', 'Gaming', '2 in 1 Convertible', 'Netbook', 'Workstation', 'Other'])
inches = st.slider("Taille de l’écran (pouces)", 10.0, 18.0, 15.6)
resolution_x = st.number_input("Résolution - Largeur (ex: 1920)", value=1920)
resolution_y = st.number_input("Résolution - Hauteur (ex: 1080)", value=1080)
ram = st.slider("RAM (Go)", 2, 64, 8)
storage = st.slider("Stockage total (Go)", 128, 2048, 512)
weight = st.number_input("Poids (kg)", value=1.5)
os = st.selectbox("Système d’exploitation", ['Windows 10', 'macOS', 'No OS', 'Windows 7', 'Other'])
cpu_brand = st.selectbox("Processeur", ['Intel', 'AMD', 'Samsung', 'Other'])
gpu_brand = st.selectbox("Carte graphique", ['Intel', 'Nvidia', 'AMD', 'ARM', 'Other'])

# Préparation des features pour le modèle
def prepare_input():
    input_dict = {
        'Inches': inches,
        'Ram': ram,
        'Weight': weight,
        'Resolution_X': resolution_x,
        'Resolution_Y': resolution_y,
        'TotalMemory': storage,
        'Company_' + company: 1,
        'TypeName_' + typename: 1,
        'OpSys_' + os: 1,
        'Cpu_Brand_' + cpu_brand: 1,
        'Gpu_Brand_' + gpu_brand: 1
    }

    # Liste des colonnes du modèle (à adapter selon ton dataset d’origine)
    all_columns = model.feature_names_in_

    # Créer une ligne avec 0 partout sauf les features spécifiées
    input_vector = pd.DataFrame(np.zeros((1, len(all_columns))), columns=all_columns)
    for key, value in input_dict.items():
        if key in input_vector.columns:
            input_vector[key] = value
    return input_vector

if st.button("Prédire le prix 💰"):
    input_data = prepare_input()
    prediction = model.predict(input_data)[0]
    st.success(f"💸 Prix estimé : **{prediction:,.0f} CFA**")
