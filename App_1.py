import streamlit as st
import pickle
import numpy as np

# Charger le modèle
model = pickle.load(open('modele_laptops.pkl', 'rb'))

# Titre de l'application
st.title("Prédiction du prix d'un ordinateur portable 💻")

# Formulaire utilisateur
company = st.selectbox("Marque", ['Dell', 'Apple', 'HP', 'Acer', 'Asus', 'Lenovo'])
typename = st.selectbox("Type", ['Ultrabook', 'Notebook', 'Gaming', '2 in 1 Convertible', 'Workstation'])
ram = st.slider("RAM (en Go)", 2, 64, step=2)
weight = st.number_input("Poids (en kg)", min_value=0.5, max_value=5.0, step=0.1)
touchscreen = st.selectbox("Écran tactile", ['Non', 'Oui'])
ips = st.selectbox("Technologie IPS", ['Non', 'Oui'])
screen_size = st.slider("Taille écran (en pouces)", 10.0, 20.0, step=0.1)
resolution = st.selectbox("Résolution écran", ['1920x1080', '1366x768', '1600x900', '3840x2160'])
cpu = st.selectbox("Processeur", ['Intel Core i5', 'Intel Core i7', 'Intel Core i3', 'AMD Ryzen 5', 'AMD Ryzen 7'])
hdd = st.slider("HDD (Go)", 0, 2000, step=128)
ssd = st.slider("SSD (Go)", 0, 2000, step=128)
gpu = st.selectbox("Carte graphique", ['Intel', 'Nvidia', 'AMD'])
os = st.selectbox("Système d’exploitation", ['Windows', 'Mac', 'Linux', 'Others'])

# Bouton de prédiction
if st.button('Prédire le prix'):
    # Conversion des données
    touchscreen = 1 if touchscreen == 'Oui' else 0
    ips = 1 if ips == 'Oui' else 0
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2 + Y_res**2) ** 0.5) / screen_size
    
    input_data = np.array([[company, typename, ram, weight, touchscreen, ips, ppi,
                            cpu, hdd, ssd, gpu, os]])

    # Encodage si nécessaire (OneHot/LabelEncoder)
    # ⚠️ Adapter cette partie en fonction de votre preprocessing
    # Ici on suppose que vous avez un pipeline dans le modèle

    prediction = model.predict(input_data)
    st.success(f"💰 Prix estimé : {int(prediction[0]):,} CFA")
