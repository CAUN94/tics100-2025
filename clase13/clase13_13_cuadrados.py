"""
👤 Detección de rostros en una imagen con Haar Cascade.

Este programa:
1. Carga 'imagen.jpg' desde el directorio actual.
2. Usa el clasificador Haar para encontrar rostros.
3. Dibuja rectángulos en los rostros detectados.
4. Muestra y guarda la imagen resultante como 'imagen_rostros.jpg'.
5. Muestra en consola cuántas personas hay en la imagen.
"""

import cv2

# Cargar la imagen
imagen = cv2.imread("imagen.jpg")
if imagen is None:
    print("❌ No se encontró 'imagen.jpg'")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Cargar el clasificador Haar de rostros
clasificador = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Detectar rostros
rostros = clasificador.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5)

# Mostrar cantidad de rostros
cantidad = len(rostros)
print(f"✅ Se detectaron {cantidad} rostro(s) en la imagen.")

# Dibujar rectángulos en los rostros detectados
for (x, y, w, h) in rostros:
    cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Guardar imagen resultante
cv2.imwrite("imagen_rostros.jpg", imagen)

# Mostrar imagen con conteo en el título
cv2.imshow(f"Rostros detectados: {cantidad}", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
