import numpy as np
import matplotlib.pyplot as plt

# Mostrar opciones
print("Selecciona el tipo de función que quieres graficar:")
print("1. Lineal")
print("2. Cuadrática")
print("3. Seno")
print("4. Coseno")

opcion = input("Ingresa el número de la opción (1-4): ")

# Generar valores de x
x = np.linspace(-10, 10, 400)

# Evaluar función según la opción
if opcion == "1":
    y = 2 * x + 3
    titulo = "Función Lineal: y = 2x + 3"
elif opcion == "2":
    y = x**2 - 4*x + 1
    titulo = "Función Cuadrática: y = x² - 4x + 1"
elif opcion == "3":
    y = np.sin(x)
    titulo = "Función Seno: y = sin(x)"
elif opcion == "4":
    y = np.cos(x)
    titulo = "Función Coseno: y = cos(x)"
else:
    print("Opción inválida. Mostrando función seno por defecto.")
    y = np.sin(x)
    titulo = "Función Seno: y = sin(x) (por defecto)"

# Graficar
plt.figure(figsize=(8, 4))
plt.plot(x, y, label=titulo, color='blue')
plt.title(titulo)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()
