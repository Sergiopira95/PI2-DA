import streamlit as st

st.set_page_config(
    page_title="Portada",
    page_icon="📉",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.subheader(':satellite_antenna: Reporte PI2 DA - Telecomunicaciones Argentina') #Titulo del Dashboard
# st.markdown('***')
st.image("img/portada.jpeg")
st.markdown('###')
import streamlit as st

# Título de la aplicación
st.title('Análisis del Sector de Telecomunicaciones en Argentina')

# Introducción
st.subheader('Introducción')

st.write("""
Estimados stakeholders,

Es un placer presentarles el análisis integral que he realizado sobre el sector de telecomunicaciones en Argentina, con un enfoque especial en el comportamiento y tendencias del acceso a internet, así como otros servicios de comunicación fundamentales. La industria de las telecomunicaciones en nuestro país ha sido un pilar esencial para la conexión y el desarrollo de la sociedad, no solo facilitando la comunicación diaria entre millones de personas, sino también soportando la infraestructura que sustenta el crecimiento de las empresas y el acceso a servicios educativos, comerciales y de entretenimiento.

A través de este análisis, buscamos ofrecer una visión clara sobre el estado actual de los servicios de telecomunicaciones, con énfasis en la penetración de internet y su uso en el país. Este informe también destaca las oportunidades clave para la empresa, con el fin de mejorar la calidad de los servicios brindados, identificar nuevas áreas de crecimiento y, lo más importante, permitirnos ofrecer soluciones personalizadas a los clientes que respondan a sus necesidades y expectativas.

Nuestro objetivo es proporcionar una guía precisa y fundamentada que les permita tomar decisiones informadas para fortalecer la posición de la empresa en el mercado, aumentar la satisfacción del cliente y garantizar un crecimiento sostenible en este dinámico sector.
""")

