"""
🖼️ Análisis básico de imágenes:
Este programa carga una imagen llamada 'imagen.jpg', la convierte a escala de grises,
aplica un desenfoque, encuentra sus bordes con Canny y genera una imagen binarizada 
mediante un umbral.
"""

import cv2
import matplotlib.pyplot as plt

# Cargar imagen
imagen = cv2.imread("imagen.jpg")
if imagen is None:
    print("❌ Error: No se encontró la imagen 'imagen.jpg'")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar desenfoque gaussiano para suavizar
desenfoque = cv2.GaussianBlur(gris, (5, 5), 0)

# Detección de bordes con Canny
bordes = cv2.Canny(desenfoque, 100, 200)

# Umbral binario simple
_, umbral = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY)

# Mostrar los resultados
fig, axs = plt.subplots(1, 4, figsize=(14, 5))

axs[0].imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
axs[0].set_title("Imagen Original")
axs[0].axis("off")

axs[1].imshow(gris, cmap='gray')
axs[1].set_title("Escala de Grises")
axs[1].axis("off")

axs[2].imshow(bordes, cmap='gray')
axs[2].set_title("Bordes (Canny)")
axs[2].axis("off")

axs[3].imshow(umbral, cmap='gray')
axs[3].set_title("Umbral Binario")
axs[3].axis("off")

plt.tight_layout()
plt.show()
