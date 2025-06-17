import numpy as np
import matplotlib.pyplot as plt

print("📌 Simulación de movimiento rectilíneo (MRU y MRUA)")

tipo = input("¿Qué tipo de movimiento deseas simular? (mru / mrua): ").lower()

if tipo not in ["mru", "mrua"]:
    print("❌ Tipo de movimiento no reconocido.")
    exit()

x0 = float(input("📍 Posición inicial x₀ (m): "))
v0 = float(input("🚀 Velocidad inicial v₀ (m/s): "))
t_max = float(input("⏱️ Tiempo total de simulación (s): "))
t = np.linspace(0, t_max, 200)

if tipo == "mru":
    # MRU: x = x0 + v*t
    x = x0 + v0 * t
    v = np.full_like(t, v0)
    titulo = "MRU (Velocidad constante)"
elif tipo == "mrua":
    a = float(input("🧲 Aceleración a (m/s²): "))
    # MRUA: x = x0 + v0*t + 0.5*a*t²
    x = x0 + v0 * t + 0.5 * a * t**2
    v = v0 + a * t
    titulo = "MRUA (Con aceleración)"

# Graficar posición
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(t, x, label='Posición x(t)', color='blue')
plt.xlabel("Tiempo (s)")
plt.ylabel("Posición (m)")
plt.title(f"📍 Posición vs Tiempo\n{titulo}")
plt.grid(True)
plt.legend()

# Graficar velocidad
plt.subplot(1, 2, 2)
plt.plot(t, v, label='Velocidad v(t)', color='green')
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (m/s)")
plt.title(f"🚀 Velocidad vs Tiempo\n{titulo}")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
