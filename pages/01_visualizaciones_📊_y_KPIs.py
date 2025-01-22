# Importación de librerías
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

# Cargamos los dataframes
df_accesos_tec = pd.read_csv("./datasets/df7_accesos_tec.csv")
low_penetration_df = pd.read_csv("./datasets/df_kpi1.csv")
low_speed_df = pd.read_csv('./datasets/df_kpi2.csv')

# Convertir los nombres de las columnas a formato estándar si es necesario
df_accesos_tec.columns = df_accesos_tec.columns.str.strip().str.lower().str.replace(" ", "_")

    
# Crear selectores para el usuario
year = st.selectbox("Selecciona el año:", sorted(df_accesos_tec['año'].unique()))
trimester = st.selectbox("Selecciona el trimestre:", sorted(df_accesos_tec['trimestre'].unique()))
province = st.selectbox("Selecciona la Provincia:",sorted(df_accesos_tec['provincia'].unique()))
    
# Filtrar datos
filtered_data = df_accesos_tec[(df_accesos_tec['provincia'] == province)]
filtered_data_kpi1 = low_penetration_df[(low_penetration_df['Provincia'] == province)]
filtered_data_kpi2 = low_speed_df[(low_speed_df['Provincia'] == province)]
    
# Crear una columna total para sumar todas las tecnologías
tech_columns = ['adsl', 'cablemodem', 'fibra_óptica', 'wireless', 'otros']
filtered_data['total_tecnologias'] = filtered_data[tech_columns].sum(axis=1)
    
# Crear una gráfica de barras apiladas para la distribución de tecnologías por provincia
st.subheader(f"Distribución del Acceso a Internet por Tecnología para la provincia de {province}")
fig = px.bar(
    filtered_data, x='año', y= tech_columns,
    labels={"value": "Cantidad de accesos", "año": "Año"},
    color_discrete_sequence=px.colors.qualitative.Pastel
            )
    
# Mostrar la gráfica
st.plotly_chart(fig)

##############################

# Función para aplicar formato condicional al color de los KPIs
def formato_condicional(valor, criterio):
    color = "green" if valor >= criterio else "red"
    return f'<p style="font-size: 26px; color:{color};"> {valor}%</p>'

criterio_kpi1 = 2.0
valor_kpi1 = filtered_data_kpi1['KPI_Aumento_Acceso'].iloc[-1]
criterio_kpi2 = 10.0
valor_kpi2 = filtered_data_kpi2['KPI_Aumento_Acceso'].iloc[-1]

column1, column2, column3= st.columns(3)
with column1:
    st.write(f"Aumento 2% - Accesos a Internet para la provincia {province}:")
    st.markdown(formato_condicional(valor_kpi1, criterio_kpi1), unsafe_allow_html=True)
with column2:
    st.write(f"Aumento 10% - Aumento Velocidad en la provincia {province}:")
    st.markdown(formato_condicional(valor_kpi2, criterio_kpi2), unsafe_allow_html=True)
