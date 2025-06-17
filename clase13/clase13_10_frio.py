import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import datetime

# Obtener hora actual
hora_actual = datetime.datetime.now().hour + datetime.datetime.now().minute / 60
intensidad = np.clip((np.sin((hora_actual / 24) * 2 * np.pi) + 1) / 2, 0.2, 1.0)
# Esto hace que la intensidad del oleaje sea mayor al mediodía y menor de noche

# Crear figura y eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Crear malla
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Configurar ejes
ax.set_zlim(-2, 2)
ax.set_title(f"🌊 Olas 3D (Hora actual: {hora_actual:.2f})", fontsize=12)

# Función de actualización
def update(frame):
    ax.clear()
    t = frame / 10
    Z = intensidad * np.sin(X + t) * np.cos(Y + t)
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_zlim(-2, 2)
    ax.set_title(f"🌊 Olas 3D dinámicas - t = {t:.2f} | Intensidad: {intensidad:.2f}", fontsize=10)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Altura")

# Animar
ani = FuncAnimation(fig, update, frames=100, interval=100)

# Mostrar
plt.show()
