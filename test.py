import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Prediksi Penyakit Jantung",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Sistem Prediksi Penyakit Jantung by Muhammad Fitra',

                           [
                            'Prediksi Penyakit Jantung',
                            ],
                           menu_icon='hospital-fill',
                           icons=[ 'heart'],
                           default_index=0)


# Heart Disease Prediction Page
if selected == 'Prediksi Penyakit Jantung':

    # Page title
    st.title('Prediksi Penyakit Jantung by Muhammad Fitra')

# Baris 1
col1, col2, col3 = st.columns(3)
with col1:
    age = st.text_input('Umur. #age')
with col2:
    sex = st.text_input('Jenis Kelamin (1 = Laki-Laki, 0 = Perempuan). #sex')
with col3:
    cp = st.text_input('Jenis Nyeri Dada (0 = Typical Angina, 1 = Atypical Angina, 2 = Non-anginal Pain, 3 = Asymptomatic). #cp')

# Baris 2
col1, col2, col3 = st.columns(3)
with col1:
    trestbps = st.text_input('Tekanan darah saat istirahat (mm Hg). #trestbps')
with col2:
    chol = st.text_input('Kadar kolesterol dalam darah (mg/dl). #chol')
with col3:
    fbs = st.text_input('Kadar gula darah saat puasa > 120 mg/dl? (1 = Ya, 0 = Tidak). #fbs')

# Baris 3
col1, col2, col3 = st.columns(3)
with col1:
    restecg = st.text_input('Hasil elektrokardiografi (EKG) saat istirahat (0=Normal, 1=Memiliki kelainan gelombang ST-T, 2=Menunjukkan hipertrofi ventrikel kiri(LVH)). #restecg')
with col2:
    thalach = st.text_input('Detak jantung maksimum. #thalach')
with col3:
    exang = st.text_input('Nyeri dada akibat olahraga (1 = Ya, 0 = Tidak). #exang')

# Baris 4
col1, col2, col3 = st.columns(3)
with col1:
    oldpeak = st.text_input('Penurunan segmen ST pada EKG saat olahraga dibandingkan dengan saat istirahat. #oldpeak')
with col2:
    slope = st.text_input('Kemiringan segmen ST pada EKG saat puncak olahraga. (0 = Naik, 1 = Datar, 2 = Menurun). #slope')
with col3:
    ca = st.text_input('Jumlah pembuluh darah utama (0-3) yang terlihat melalui fluoroskopi. #ca')

# Baris 5
col1, _, _ = st.columns(3)
with col1:
    thal = st.text_input('Hasil tes thalassemia. (1=Normal, 2=Cacat Tetap, 3=Cacat Yang Muncul Hanya Saat Stres). #thal')


    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Periksa'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'Kamu Menderita Penyakit Jantung'
        else:
            heart_diagnosis = 'Kamu Tidak Menderita Penyakit Jantung'

    st.success(heart_diagnosis)

