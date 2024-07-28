import pandas as pd
import matplotlib.pyplot as plt
import math as m
import numpy as np

plt.rcParams.update({'font.size': 12})

def cargar_datos(nombre_archivo: str) -> pd.DataFrame:
    """ Carga los datos de un archivo csv y retorna el DataFrame con la información."""
    return pd.read_csv(nombre_archivo)

def histograma_descubrimiento(datos: pd.DataFrame) -> None:
    """ Calcula y despliega un histograma con 30 grupos (bins) en el que debe aparecer la cantidad de planetas descubiertos por año."""
    plt.figure(figsize=(10, 6))
    datos['DESCUBRIMIENTO'].dropna().astype(int).plot.hist(bins=30)
    plt.title('Histograma de Descubrimientos de Exoplanetas por Año')
    plt.xlabel('Año de Descubrimiento')
    plt.ylabel('Cantidad de Planetas')
    plt.show()

def estado_publicacion_por_descubrimiento(datos: pd.DataFrame) -> None:
    """ Calcula y despliega un BoxPlot donde aparecen la cantidad de planetas descubiertos por año, agrupados de acuerdo con el tipo de publicación."""
    plt.figure(figsize=(10, 6))
    datos.boxplot(column='DESCUBRIMIENTO', by='ESTADO_PUBLICACION', grid=False)
    plt.title('Estado de Publicación por Año de Descubrimiento')
    plt.suptitle('')
    plt.xlabel('Estado de Publicación')
    plt.ylabel('Año de Descubrimiento')
    plt.show()

def deteccion_por_descubrimiento(datos: pd.DataFrame) -> None:
    """ Calcula y despliega un BoxPlot donde aparecen la cantidad de planetas descubiertos por año, agrupados de acuerdo con el tipo de detección."""
    plt.figure(figsize=(10, 6))
    datos.boxplot(column='DESCUBRIMIENTO', by='TIPO_DETECCION', grid=False)
    plt.title('Tipo de Detección por Año de Descubrimiento')
    plt.suptitle('')
    plt.xlabel('Tipo de Detección')
    plt.ylabel('Año de Descubrimiento')
    plt.show()

def deteccion_y_descubrimiento(datos: pd.DataFrame, anho: int) -> None:
    """ Calcula y despliega un diagrama de pie donde aparecen la cantidad de planetas descubiertos en un año particular, clasificados de acuerdo con el tipo de publicación."""
    if anho != 0:
        datos = datos[datos['DESCUBRIMIENTO'] == anho]
    
    counts = datos['ESTADO_PUBLICACION'].value_counts()
    
    plt.figure(figsize=(8, 8))
    counts.plot.pie(autopct='%1.1f%%')
    plt.title(f'Detección y Descubrimiento en {anho if anho != 0 else "Todos los Años"}')
    plt.ylabel('')
    plt.show()

def cantidad_y_tipo_deteccion(datos: pd.DataFrame) -> None:
    """ Calcula y despliega un diagrama de líneas donde aparece una línea por cada tipo de detección y se muestra la cantidad de planetas descubiertos en cada año, para ese tipo de detección."""
    deteccion_anual = datos.groupby(['DESCUBRIMIENTO', 'TIPO_DETECCION']).size().unstack(fill_value=0)
    
    plt.figure(figsize=(12, 8))
    deteccion_anual.plot()
    plt.title('Cantidad de Planetas Descubiertos por Año y Tipo de Detección')
    plt.xlabel('Año de Descubrimiento')
    plt.ylabel('Cantidad de Planetas')
    plt.legend(title='Tipo de Detección')
    plt.show()


def masa_promedio_y_tipo_deteccion(datos: pd.DataFrame) -> None:
    """ Calcula y despliega un diagrama de líneas donde aparece una línea por cada tipo de detección y se muestra la masa promedio de los planetas descubiertos en cada año, para ese tipo de detección."""
    masa_promedio_anual = datos.groupby(['DESCUBRIMIENTO', 'TIPO_DETECCION'])['MASA'].mean().unstack(fill_value=0)
    
    plt.figure(figsize=(12, 8))
    masa_promedio_anual.plot()
    plt.title('Masa Promedio de Planetas Descubiertos por Año y Tipo de Detección')
    plt.xlabel('Año de Descubrimiento')
    plt.ylabel('Masa Promedio de los Planetas')
    plt.legend(title='Tipo de Detección')
    plt.show()


def masa_planetas_vs_masa_estrellas(datos: pd.DataFrame) -> None:
    """ Calcula y despliega un diagrama de dispersión donde en el eje x se encuentra la masa de los planetas y en el eje y se encuentra el logaritmo de la masa de las estrellas."""
    plt.figure(figsize=(10, 6))
    plt.scatter(datos['MASA'], np.log(datos['MASA_ESTRELLA']))
    plt.title('Masa de Planetas vs. Logaritmo de la Masa de Estrellas')
    plt.xlabel('Masa de los Planetas')
    plt.ylabel('Logaritmo de la Masa de las Estrellas')
    plt.show()

def graficar_cielo(datos: pd.DataFrame) -> list:
    """ Calcula y despliega una imagen donde aparece un pixel por cada planeta, usando colores diferentes que dependen del tipo de detección utilizado para descubrirlo."""
    deteccion_colores = {
        'transit': 'blue',
        'radial_velocity': 'red',
        'imaging': 'green',
        'microlensing': 'purple',
        'timing': 'orange',
        'other': 'grey'
    }
    
    colores = datos['TIPO_DETECCION'].map(deteccion_colores).fillna('black')
    imagen = np.zeros((len(datos), 3), dtype=int)
    
    for i, color in enumerate(colores):
        if color == 'blue':
            imagen[i] = [0, 0, 255]
        elif color == 'red':
            imagen[i] = [255, 0, 0]
        elif color == 'green':
            imagen[i] = [0, 255, 0]
        elif color == 'purple':
            imagen[i] = [128, 0, 128]
        elif color == 'orange':
            imagen[i] = [255, 165, 0]
        elif color == 'grey':
            imagen[i] = [128, 128, 128]
        else:
            imagen[i] = [0, 0, 0]
    
    plt.figure(figsize=(10, 6))
    plt.imshow(imagen.reshape(1, -1, 3))
    plt.axis('off')
    plt.show()
    
    return imagen



def filtrar_imagen_cielo(imagen: list) -> None:
    """ Le aplica a la imagen un filtro de convolución basado en la matriz [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]"""
    filtro = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    imagen_filtrada = np.zeros_like(imagen)
    
    for i in range(1, len(imagen) - 1):
        for j in range(1, 2):
            sub_img = imagen[i-1:i+2, j-1:j+2]
            imagen_filtrada[i, j] = np.sum(sub_img * filtro)
    
    plt.figure(figsize=(10, 6))
    plt.imshow(imagen_filtrada.reshape(1, -1, 3))
    plt.axis('off')
    plt.show()


