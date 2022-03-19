import streamlit as st
import pandas as pd
import sqlite3 as sql

#DEbe poderse registrr un usuario con su nombre y buscalo en el selectbox para poder guardar
#sus efluentes y ultimos labroatorios
st.image("WAPP.png")
nombres=(['Alonso','Fernando'])
Registro=st.text_input("Nombre")
names=nombres.append(Registro)

@st.cache(allow_output_mutation=True)

user_id = st.text_input("Name")


if st.button("Add row"):
    nombres.append({"UserID": user_id, "foo": foo, "bar": bar})

st.write(pd.DataFrame(nombres))
        
ID=st.selectbox('Busca tu nombre',nombres)
