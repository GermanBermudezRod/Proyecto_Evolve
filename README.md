
# PROYECTOEVOLVE - Análisis de Ocupación Turística y Digitalización de Campings en España

## Descripción del Proyecto

Este proyecto nace en el marco de la creación de una empresa dedicada a la digitalización y automatización de campings, alojamientos rurales y complejos turísticos situados en entornos rurales en España.

El principal objetivo es realizar un análisis exploratorio de los datos de ocupación turística proporcionados por el Instituto Nacional de Estadística (INE), y estudiar la posible correlación existente entre una correcta digitalización de los establecimientos y un aumento en la facturación o en los niveles de ocupación.

Además, este proyecto pretende servir como herramienta de presentación y demostración para futuros clientes de la empresa, aportando valor desde el análisis de datos y mostrando el potencial de la digitalización en el sector turístico rural.

## Dificultades encontradas

Uno de los principales retos de este proyecto ha sido la falta de datos abiertos y específicos que midan directamente el grado de digitalización de los alojamientos rurales y campings en España.

Los datos disponibles de organismos oficiales como el INE se centran principalmente en aspectos cuantitativos de ocupación (viajeros, pernoctaciones, estancia media...), pero no existen datasets públicos que recojan indicadores de digitalización o transformación digital en estos complejos.

Este hecho refuerza todavía más el valor añadido de la empresa, al cubrir un área de necesidad no resuelta actualmente en el sector.

## Tecnologías utilizadas

- Python (procesos ETL y limpieza de datos)
- Librerías: Pandas y Numpy
- Power BI (análisis visual y creación de dashboards)

## Estructura del Proyecto

PROYECTOEVOLVE/
│
├── data/                   # Datos originales descargados del INE
│   ├── processed/          # Dataset final limpio generado automáticamente
│   └── *.csv               # Datos de ocupación hotelera, campings, etc.
│
├── src/
│   └── etl.py              # Código Python de transformación y limpieza de datos (ETL)
│
├── main.py                 # Script principal de ejecución del proceso completo
│
├── requirements.txt        # Librerías necesarias
│
└── README.md               # Documentación del proyecto

## Funcionamiento

1. Añadir los archivos `.csv` descargados en la carpeta `/data/`.
2. Ejecutar el siguiente comando:

python main.py

3. El script realiza automáticamente:
   - Limpieza de todos los datasets.
   - Unificación de datos de diferentes tipos de alojamientos.
   - Búsqueda y unión automática de todos los CSV de campings encontrados en `/data/`.
   - Generación del archivo final limpio: `/data/processed/master_dataset.csv`

4. Este archivo es posteriormente utilizado en Power BI para la creación de dashboards y análisis visual.

## Objetivos futuros del proyecto

- Incluir nuevas fuentes de datos relacionadas con digitalización (servicios online, medios de pago digitales, automatización de reservas...).
- Desarrollo de modelos predictivos.
- Creación de dashboards personalizados para cada cliente.
- Análisis sobre datos reales obtenidos de los propios clientes una vez implementados los sistemas de digitalización.

> Proyecto realizado como parte del Trabajo Final del Máster de Data Analyst (2025).
