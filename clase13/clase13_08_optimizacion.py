"""
🔎 Ejercicio: Optimización simple de funciones con Scipy

Enunciado:
Una empresa quiere optimizar sus ventas. El costo total en función de la cantidad vendida (x)
está dado por la función:

    C(x) = (x - 3)**2 + 10

Esto representa que el costo es mínimo cuando se venden cerca de 3 unidades, pero desconocemos 
exactamente cuántas unidades minimizan el costo. Usaremos `scipy.optimize.minimize` para encontrar 
el valor óptimo de x que minimiza la función de costo C(x).

Objetivo: 
- Graficar la función de costo.
- Usar `minimize` para encontrar el mínimo.
- Visualizar el punto óptimo.

Aplicaciones: 
Esta técnica se puede aplicar a problemas reales como reducción de costos, maximización de beneficios 
o ajustes de parámetros en ingeniería y ciencia de datos.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Definimos la función objetivo (costo)
def costo(x):
    return (x - 3)**2 + 10

# Usamos scipy.optimize.minimize para encontrar el mínimo
resultado = minimize(costo, x0=0)  # x0 es el valor inicial de búsqueda

# Resultados
x_optimo = resultado.x[0]
costo_minimo = resultado.fun

print(f"✅ Cantidad óptima para minimizar el costo: x = {x_optimo:.4f}")
print(f"💸 Costo mínimo alcanzado: {costo_minimo:.4f}")

# Graficamos la función y el punto mínimo
x_vals = np.linspace(-2, 8, 200)
y_vals = costo(x_vals)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label='Costo(x)', color='blue')
plt.scatter([x_optimo], [costo_minimo], color='red', label='Mínimo encontrado')
plt.title("Optimización de función de costo")
plt.xlabel("Cantidad (x)")
plt.ylabel("Costo total")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
