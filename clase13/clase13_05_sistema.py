import numpy as np
import matplotlib.pyplot as plt

print("📈 Ajuste de curvas y regresión lineal")
n = int(input("¿Cuántos puntos experimentales vas a ingresar? "))

x_vals = []
y_vals = []

print("\n🔢 Ingresa los pares (x, y):")
for i in range(n):
    x = float(input(f"x[{i+1}]: "))
    y = float(input(f"y[{i+1}]: "))
    x_vals.append(x)
    y_vals.append(y)

# Convertir a numpy arrays
x = np.array(x_vals)
y = np.array(y_vals)

# Ajuste de regresión lineal (polinomio de grado 1)
coefs = np.polyfit(x, y, 1)
pendiente, intercepto = coefs
print(f"\n📘 Ecuación ajustada: y = {pendiente:.4f}x + {intercepto:.4f}")

# Evaluar la línea ajustada
x_linea = np.linspace(min(x) - 1, max(x) + 1, 200)
y_linea = pendiente * x_linea + intercepto

# Graficar
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', label='Datos originales')
plt.plot(x_linea, y_linea, color='red', label='Regresión lineal')
plt.xlabel("x")
plt.ylabel("y")
plt.title("📊 Ajuste por regresión lineal")
plt.grid(True)
plt.legend()
plt.show()
