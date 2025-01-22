import streamlit as st
import streamlit.components.v1 as components

# Titular la pagina
st.subheader('Mapa de Telecomunicaciones en Argentina')

# Ruta al archivo HTML
html_file_path = './mapa_conexiones_internet.html'

# Leer el contenido del archivo HTML
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Mostrar el contenido HTML en Streamlit
components.html(html_content, height=450, scrolling=True)