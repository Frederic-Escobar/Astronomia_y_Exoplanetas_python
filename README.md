# Análisis de Exoplanetas

En este proyecto porviene del estudio realizado en el curso de la Universidad de los Andes sobre [Programación en Python
Universidad de los Andes](https://ingenieria.uniandes.edu.co/es/noticias/mooc-coursera-programacion-en-python), trabajarás con datos de todos los planetas extrasolares confirmados, conocidos como exoplanetas, descubiertos entre 1988 y 2018 (más de 3000). La información proviene de la base de datos Open Exoplanet Catalogue, la cual está disponible en [Kaggle](https://www.kaggle.com/mrisdal/open-exoplanet-catalogue).

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

## Requerimiento 2: Descubrimiento por estado de publicación
El segundo requerimiento es permitir relacionar los años de descubrimiento de los planetas y los tipos de publicación que se utilizaron para informar los descubrimientos. Para esto, debes crear una gráfica de tipo boxplot, usando la columna DESCUBRIMIENTO y agrupando los datos de acuerdo con la columna ESTADO_PUBLICACION. La siguiente figura muestra la apariencia de esta gráfica:
![Boxplot](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/Q1aAicPlRBSWgInD5eQUng_6fa01910ca9e47568220d7e66cedc1af_i2.png?expiry=1722297600000&hmac=yEQRjr5Ms_vPnaxXd0cPhFd2Jt076_4br6YA49SBkMw)

## Requerimiento 5: Cantidad de descubrimientos por año según el tipo de detección  
El siguiente requerimiento es explorar la relación entre la cantidad de planetas descubiertos, el tipo de detección utilizado y el año de descubrimiento. Primero, veamos la gráfica que se debes producir:
![Diagrama](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/UPp5vrOYTre6eb6zmI63bQ_79ac78a692654df885fcb77be3525424_i6_v2.png?expiry=1722384000000&hmac=13qQXmnPzFbSxHUH8OQdE1L2d--bIP37Y_q4Bqm-m5E)

## Requerimiento 7: Masa de los planetas vs masa de la estrella más cercana
En esta parte de la aplicación, vas a generar una gráfica de dispersión para analizar la masa de los planetas vs. la masa de la estrella más cercana a cada uno. La siguiente figura muestra la apariencia de la gráfica que deberías obtener:

![Dispersión](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/63R6VHHqRuy0elRx6tbsWw_da217081ef9444b3833c4937c3244089_i8.png?expiry=1722384000000&hmac=sW4N7Cf_ZHYw8mnOtbhkEBk3xTNnSVP56Nn9mbr030M)
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
