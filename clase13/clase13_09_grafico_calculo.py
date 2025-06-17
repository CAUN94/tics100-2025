# 🧮 Visualización avanzada con funciones simbólicas y punto animado
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sympy as sp

# Crear símbolo simbólico
x = sp.symbols('x')
# Definir función base (puedes cambiarla por otra curva)
f_expr = sp.sin(x) * sp.exp(-x / 3)
# Ejemplo de función cúbica (descomentar para usar)
# f_expr = x**3 - 6*x**2 + 4*x + 12
# Ejemplo de función cuadrática (descomentar para usar)
# f_expr = x**2 - 4*x + 3
# Ejemplo de función racional (descomentar para usar)
# f_expr = (x**2 - 1) / (x - 2)
# Ejemplo de función exponencial (descomentar para usar)
# f_expr = sp.exp(x) - 5
# Ejemplo de función logarítmica (descomentar para usar)
# f_expr = sp.log(x + 3) + 2

# Derivada e integral
f_deriv = sp.diff(f_expr, x)
f_integ = sp.integrate(f_expr, x)

# Convertir a funciones numéricas con NumPy
f = sp.lambdify(x, f_expr, modules=['numpy'])
df = sp.lambdify(x, f_deriv, modules=['numpy'])
F = sp.lambdify(x, f_integ, modules=['numpy'])

# Valores de X
x_vals = np.linspace(-2, 6, 400)

# Evaluar funciones
y_f = f(x_vals)
y_df = df(x_vals)
y_F = F(x_vals)

# Configurar gráfico
fig, axs = plt.subplots(3, 1, figsize=(10, 12), sharex=True)
titles = ["f(x): Función original", "f'(x): Derivada", "∫f(x)dx: Integral"]
lines = []
points = []

for ax, y, title in zip(axs, [y_f, y_df, y_F], titles):
    ax.plot(x_vals, y, 'lightgray', linewidth=2, label='Curva completa')  # Curva fija
    line, = ax.plot([], [], 'b-', linewidth=2)  # Línea animada (opcional)
    point, = ax.plot([], [], 'ro', label='Punto en movimiento')  # Punto animado
    ax.set_title(title)
    ax.legend()
    ax.grid(True)
    lines.append(line)
    points.append(point)

# Inicializar animación
def init():
    for line, point in zip(lines, points):
        line.set_data([], [])
        point.set_data([], [])
    return lines + points

# Animación
def animate(i):
    x_i = x_vals[i]
    y_i = [f(x_i), df(x_i), F(x_i)]
    for j, point in enumerate(points):
        point.set_data([x_i], [y_i[j]])
        lines[j].set_data(x_vals[:i], [f, df, F][j](x_vals[:i]))
    return lines + points

ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=len(x_vals), interval=20, blit=True)

plt.tight_layout()
plt.show()
