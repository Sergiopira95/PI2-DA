
# Análisis de Telecomunicaciones en Argentina

## Autor: Sergio Piratoba

![Telec1](./img/portada.jpeg)

### Introducción

Las telecomunicaciones son una parte esencial de la infraestructura moderna, facilitando la transmisión de información y la conexión entre personas, empresas y dispositivos a escala global. En Argentina, el acceso a estos servicios ha crecido considerablemente en los últimos años. Para el año 2020, el país contaba con 62,12 millones de conexiones activas, posicionándose como uno de los líderes regionales en este sector.

El presente proyecto tiene como objetivo realizar un análisis exhaustivo del sector de telecomunicaciones en Argentina, con un enfoque particular en el acceso a internet. Este análisis ayudará a identificar oportunidades de mejora, tanto en la calidad de los servicios ofrecidos como en las estrategias de expansión, permitiendo a la empresa de telecomunicaciones mejorar su competitividad y servicio.

---

### Contenido del Repositorio

1. **`notebooks/`**: Contiene el análisis exploratorio de datos (EDA) realizado. Cada paso está documentado en celdas Markdown dentro del notebook, con conclusiones claras basadas en los gráficos y análisis de datos.
   - `ENACOM_data_EDA.ipynb`: Análisis Exploratorio de Datos, cubriendo aspectos como la detección de valores faltantes, outliers y registros duplicados. Se incluyen gráficos descriptivos para interpretar los datos de ENACOM de manera visual.
   
2. **`dashboards/`**: Dashboard interactivo desarrollado para analizar y visualizar el comportamiento de las telecomunicaciones en Argentina, enfocado en el acceso a internet por provincia. 
   - Filtros interactivos para explorar los datos por provincia y servicio de telecomunicaciones.
   - Representación gráfica de KPIs clave para el sector.


---

### Descripción del Problema

#### Contexto

Las telecomunicaciones en Argentina han experimentado un crecimiento constante, impulsado en gran medida por la creciente demanda de acceso a internet y la evolución tecnológica que permite nuevas formas de comunicación. Con 62,12 millones de conexiones reportadas en 2020, es crucial que las empresas del sector sigan innovando y mejorando la calidad de sus servicios.

El internet se ha convertido en el medio de comunicación dominante, facilitando el trabajo, la educación y el entretenimiento. Para las empresas proveedoras de servicios de telecomunicaciones, es fundamental no solo garantizar un servicio estable y de calidad, sino también explorar nuevas oportunidades de crecimiento, especialmente en áreas donde la penetración de internet es menor.

#### Rol a Desarrollar

En este contexto, el análisis de los datos provistos por ENACOM permitirá entender el comportamiento del acceso a internet en las diferentes provincias de Argentina, así como los otros servicios de telecomunicaciones como la telefonía fija y móvil. El objetivo es ayudar a la empresa a identificar oportunidades de expansión y personalización de sus servicios, con el fin de mejorar la calidad percibida por los usuarios y aumentar su participación en el mercado.

---

### Propuesta de Trabajo

#### 1. Exploratory Data Analysis (EDA)

El análisis exploratorio de datos se enfoca en:
- **Identificación de valores faltantes**: Análisis de datos incompletos y cómo tratarlos.
- **Detección de valores atípicos**: Identificación de outliers que pueden afectar las conclusiones.
- **Visualización de los datos**: Uso de gráficos descriptivos como histogramas, mapas de calor y gráficos de barras para entender mejor el comportamiento de los datos por provincia y tipo de servicio.

Cada paso del EDA se encuentra documentado dentro del notebook, con explicaciones detalladas sobre las decisiones tomadas.

#### 2. Dashboard Interactivo

El dashboard incluye:
- Filtros para seleccionar provincias y tipo de servicio (internet, telefonía fija, móvil).
- Visualización clara y estética que permite interpretar fácilmente los datos.
- Representación de KPIs en gráficos interactivos, mostrando las oportunidades de crecimiento por provincia.

### 3. Indicadores Claves de Rendimiento (KPIs)


KPI :one: : **Acceso al servicio de Internet**

*  Métrica: Esta métrica se basa en medir el incremento porcentual del acceso al servicio de internet en cada provincia, calculando el número de hogares con acceso a internet por cada 100 hogares.

* Datos Necesarios: Número de hogares con acceso a internet en el trimestre actual y número proyectado de hogares con acceso a internet para el próximo trimestre.

* Objetivo: Aumentar en un 2% el número de hogares con acceso a internet por cada 100 hogares en cada provincia para el próximo trimestre.
  
  

KPI :two: : **Acceso al servicio de Fibra Óptica**

*  Métrica: Esta métrica se basa en medir el incremento porcentual del acceso al servicio de Fibra Óptica en cada provincia.
* Datos Necesarios: Número de hogares con acceso al servicio de Fibra Óptica en el trimestre actual y número proyectado de hogares con acceso al servicio de Fibra Óptica para el próximo trimestre.

* Objetivo: Aumentar en un 4% el número de hogares con acceso al servicio de Fibra Óptica en cada provincia para el próximo trimestre.

KPI :three: : **Acceso a conexiones mayores a 20 Mbps**

*  Métrica: Esta métrica se basa en medir el incremento porcentual de las conexiones de internet con velocidades mayores a 20 Mbps en cada provincia.

* Datos Necesarios: Número de conexiones actuales con velocidades mayores a 20 Mbps en el trimestre actual y número proyectado de conexiones con velocidades mayores a 20 Mbps para el próximo trimestre.

* Objetivo: Aumentar en un 10% las conexiones mayores a 20 Mbps para las provincias que tienen baja velocidad de conexión

#### 4. Análisis de Resultados

El análisis de los KPIs y los gráficos generados permitirá a la empresa identificar:
- Provincias con mayor potencial de expansión para el acceso a internet.
- Oportunidades de mejora en la calidad del servicio en áreas específicas.
- Comparativas de crecimiento entre distintos servicios de telecomunicaciones.

---

### Conclusión

Este análisis ofrece una visión clara y detallada del comportamiento del sector de telecomunicaciones en Argentina, ayudando a la empresa a tomar decisiones informadas sobre sus estrategias de crecimiento y mejora de calidad. Las oportunidades detectadas a través del análisis exploratorio y los KPIs propuestos permitirán a la empresa mejorar su oferta de servicios y ofrecer soluciones más personalizadas a sus clientes.
