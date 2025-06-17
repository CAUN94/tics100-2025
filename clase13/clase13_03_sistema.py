import numpy as np

print("🔢 Resolución de sistemas de ecuaciones lineales Ax = b")
print("¿Cuántas incógnitas tiene tu sistema? (2 o 3)")
n = int(input("Ingresa 2 o 3: "))

if n not in [2, 3]:
    print("❌ Solo se permite 2 o 3 incógnitas.")
    exit()

# Ingreso de matriz A
print("\n🧮 Ingresa los coeficientes de la matriz A (uno por uno):")
A = []
for i in range(n):
    fila = []
    for j in range(n):
        val = float(input(f"A[{i+1}][{j+1}] = "))
        fila.append(val)
    A.append(fila)

# Ingreso del vector b
print("\n🎯 Ingresa los valores del vector b:")
b = []
for i in range(n):
    val = float(input(f"b[{i+1}] = "))
    b.append(val)

# Conversión a arrays de NumPy
A = np.array(A)
b = np.array(b)

# Mostrar matriz A y vector b
print("\n🧾 Sistema ingresado:")
print("Matriz A:")
print(A)
print("\nVector b:")
print(b)

# Mostrar ecuaciones representadas
print("\n📘 Sistema de ecuaciones:")
for i in range(n):
    ecuacion = " + ".join([f"{A[i][j]}*x{j+1}" for j in range(n)])
    print(f" {ecuacion} = {b[i]}")

# Resolución del sistema
print("\n⚙️ Resolviendo el sistema Ax = b...")
try:
    x = np.linalg.solve(A, b)
    print("✅ Solución encontrada:")
    for i, val in enumerate(x):
        print(f"  x{i+1} = {val:.4f}")
except np.linalg.LinAlgError as e:
    print("❌ No se pudo resolver el sistema:", e)
