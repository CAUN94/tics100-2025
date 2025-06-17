import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetros
N = 50              # Tamaño de la cuadrícula
steps = 100         # Cuántos frames animar
probabilidad = 0.4  # Probabilidad de que el agua avance

# Estados:
# 0 = seco, 1 = húmedo (nuevo), 2 = saturado
grid = np.zeros((N, N), dtype=int)

# Iniciar con una gota en el centro
center = N // 2
grid[center, center] = 1

# Función para actualizar la cuadrícula
def update(frame):
    global grid
    new_grid = grid.copy()

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if grid[i, j] == 0:
                vecinos = grid[i-1:i+2, j-1:j+2]
                if np.any(vecinos == 1):
                    if np.random.rand() < probabilidad:
                        new_grid[i, j] = 1
            elif grid[i, j] == 1:
                new_grid[i, j] = 2

    grid[:] = new_grid
    ax.clear()
    ax.imshow(grid, cmap=cmap, vmin=0, vmax=2)
    ax.set_title(f"Gota de agua - paso {frame} (prob: {probabilidad})")
    ax.axis('off')

# Crear la visualización
fig, ax = plt.subplots()
cmap = plt.cm.get_cmap('Blues', 3)  # 3 niveles de azul: seco, húmedo, saturado
ani = FuncAnimation(fig, update, frames=steps, interval=200)

plt.show()
