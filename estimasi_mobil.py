import pickle
import streamlit as st

model = pickle.load(open('estimasi_Mobil.sav', 'rb'))
st.title('Estimasi Harga Mobil Bekas Toyota')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Jarak Tempuh Mobil (Miles)')
tax = st.number_input('Input Pajak Mobil (Pounds)')
mpg = st.number_input('Input Konsumsi BBM Mobil')
engineSize = st.number_input('Input Engine Size (Litres)')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize ]]
    ) 
    st.write ('Estimasi Harga Mobil Bekas dalam Pounds : ', predict)
    st.write('Estimasi Harga Mobil Bekas dalam IDR (Juta) :', predict*18738)
    