import streamlit as st

# Título de la app
st.title("Curso Udem")

# Mensaje de introducción
st.write("Interacción con los botones.")

# Mostrar un "dataframe ficticio" (a modo de ejemplo)
st.text("dataframe ficticio")

# Funciones para los botones
def valorado():
    st.write("Has hecho clic en 'Valorar'.")

def borrar():
    st.write("Has hecho clic en 'Borrar'.")

def enviar():
    st.write("Has hecho clic en 'Enviar'.")

# Crear los botones
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Valorar"):
        valorado()

with col2:
    if st.button("Borrar"):
        borrar()

with col3:
    if st.button("Enviar"):
        enviar()
