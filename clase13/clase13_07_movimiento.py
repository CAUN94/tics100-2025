import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

print("📌 Simulación animada de MRU / MRUA")

tipo = input("¿Qué tipo de movimiento deseas simular? (mru / mrua): ").lower()

if tipo not in ["mru", "mrua"]:
    print("❌ Tipo no válido.")
    exit()

x0 = float(input("📍 Posición inicial x₀ (m): "))
v0 = float(input("🚀 Velocidad inicial v₀ (m/s): "))
t_max = float(input("⏱️ Tiempo total de simulación (s): "))
fps = 30  # cuadros por segundo
frames = int(t_max * fps)
t = np.linspace(0, t_max, frames)

if tipo == "mru":
    x = x0 + v0 * t
    titulo = "MRU - Movimiento Rectilíneo Uniforme"
elif tipo == "mrua":
    a = float(input("🧲 Aceleración a (m/s²): "))
    x = x0 + v0 * t + 0.5 * a * t**2
    titulo = "MRUA - Movimiento Rectilíneo Uniformemente Acelerado"

# --- Crear gráfico
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, t_max)
ax.set_ylim(min(x) - 1, max(x) + 1)
ax.set_xlabel("⏱️ Tiempo (s)")
ax.set_ylabel("📍 Posición (m)")
ax.set_title(titulo)
ax.plot(t, x, label="Posición", color='blue')
punto, = ax.plot([], [], 'ro', label="Objeto en movimiento")
ax.legend()

# --- Función de actualización
def animar(i):
    punto.set_data([t[i]], [x[i]])  # ← CORREGIDO AQUÍ
    return punto,

# --- Animación
ani = FuncAnimation(fig, animar, frames=len(t), interval=1000/fps, blit=True)
plt.grid(True)
plt.tight_layout()
plt.show()
