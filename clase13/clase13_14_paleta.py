"""
🎨 Reconocimiento de colores dominantes en una imagen con K-Means

Este programa:
1. Carga 'imagen.jpg' desde el directorio actual.
2. Redimensiona la imagen para procesamiento rápido.
3. Usa K-Means (con sklearn) para identificar los n colores más frecuentes.
4. Muestra y guarda una paleta de colores generada.
"""

import cv2
import numpy as np
from sklearn.cluster import KMeans
from sklearn import datasets, model_selection, metrics
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

# Parámetros
N_COLORES = 5  # Número de colores dominantes a detectar

# Cargar imagen
imagen = cv2.imread("imagen.jpg")
if imagen is None:
    print("❌ No se encontró 'imagen.jpg'")
    exit()

# Redimensionar para acelerar el procesamiento
imagen = cv2.resize(imagen, (200, 200))
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

# Convertir la imagen a un arreglo 2D (píxeles como puntos)
pixeles = imagen_rgb.reshape((-1, 3))

# Aplicar K-Means
kmeans = KMeans(n_clusters=N_COLORES, n_init='auto')
kmeans.fit(pixeles)

# Obtener los colores y sus proporciones
colores = kmeans.cluster_centers_.astype(int)
labels = kmeans.labels_

# Calcular proporciones de cada color
proporciones = np.bincount(labels) / len(labels)

# Crear una paleta de colores
paleta = np.zeros((50, 300, 3), dtype=np.uint8)
pos_inicio = 0

for i, (color, prop) in enumerate(zip(colores, proporciones)):
    ancho = int(prop * 300)
    paleta[:, pos_inicio:pos_inicio + ancho] = color
    pos_inicio += ancho

# Mostrar y guardar la paleta
plt.figure(figsize=(6, 2))
plt.axis("off")
plt.imshow(paleta)
plt.title("🎨 Colores dominantes")
plt.savefig("paleta_colores.jpg")
plt.show()
