# Análisis de Exoplanetas

En este proyecto, trabajarás con datos de todos los planetas extrasolares confirmados, conocidos como exoplanetas, descubiertos entre 1988 y 2018 (más de 3000). La información proviene de la base de datos Open Exoplanet Catalogue, la cual está disponible en [Kaggle](https://www.kaggle.com/mrisdal/open-exoplanet-catalogue).

## Descripción del Proyecto

El archivo `exoplanetas.csv` contiene una versión simplificada de los datos originales. En este archivo:

- Se han suprimido los planetas que no han sido confirmados.
- Se han eliminado algunas columnas para simplificar el análisis.
- Se han modificado las clasificaciones de valores numéricos a valores categóricos.

Con este conjunto de datos, podrás convertirte en un explorador espacial analizando las características de los exoplanetas descubiertos. Los campos de los datos incluyen:

- Atributos de estrellas
- Atributos de planetas
- Métodos de descubrimiento
- Fechas de los descubrimientos

## Requerimientos

El primer requerimiento de la aplicación es calcular y graficar un histograma que muestre cuántos planetas fueron descubiertos a lo largo de los años. Para ello, debes:

1. Crear una gráfica de tipo histograma (`hist`) utilizando los valores de la columna `DESCUBRIMIENTO`.
2. El histograma debe separar los datos en 30 grupos (bins), permitiendo apreciar la cantidad de planetas descubiertos cada año entre 1998 y 2018.

A continuación, se muestra un ejemplo de cómo debería verse la gráfica resultante:

![Histograma de Descubrimientos](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/g_TtkUT9Tre07ZFE_W63tA_89374cea161043108e07b9ed4bb17e18_i1.png?expiry=1722297600000&hmac=dz-2Jk_9AwuHxk36E1XIghl5g6lWhhVAo0mrHVhfc8w)

## Estructura del Proyecto

- `exoplanetas.csv`: Archivo con los datos simplificados de los exoplanetas.
- `notebooks/`: Carpeta para cuadernos Jupyter (si aplicable) para el análisis de datos.
- `scripts/`: Carpeta para scripts de Python para procesar y analizar los datos.
- `README.md`: Este archivo, proporcionando información sobre el proyecto.

## Requisitos

Para trabajar en este proyecto, necesitarás tener instalado:

- Python 3.x
- Pandas
- NumPy
- Matplotlib (para visualización)
- Jupyter Notebook (opcional, para cuadernos)

Puedes instalar las dependencias usando pip:

```bash
pip install pandas numpy matplotlib jupyter
