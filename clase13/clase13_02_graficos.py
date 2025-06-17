import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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

# Crear figura y ejes
fig, ax = plt.subplots()
ax.set_title(titulo)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

# Graficar línea
linea, = ax.plot(x, y, label=titulo, color='blue')
punto, = ax.plot([], [], 'ro', label="Punto móvil")

# Definir límites
ax.set_xlim(x.min(), x.max())
ax.set_ylim(y.min() - 1, y.max() + 1)
ax.legend()

# Función de inicialización
def init():
    punto.set_data([], [])
    return punto,

# Función de animación (usando listas con un solo valor)
def animate(i):
    punto.set_data([x[i]], [y[i]])
    return punto,

# Crear animación
ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=len(x), interval=20, blit=True)

plt.show()
