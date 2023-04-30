import pickle
import streamlit as st

model = pickle.load(open('fasstfood.sav', 'rb'))

st.title('Estimasi Jumlah Kalori maknan cepat saji ')

sugar = st.number_input('Input Jumlah gula')
total_fat = st.number_input('Input total lemak')
sodium = st.number_input('Input jumlah sodium')
total_carb = st.number_input('Input total karbohidrat')

predict = ''

if st.button('Estimasi Kalori'):
    predict = model.predict(
        [[sugar, total_fat, sodium, total_carb]]
    )
    st.write ('Estimasi Jumlah Kalori (kCal) : ', predict)