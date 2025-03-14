# -*- coding: utf-8 -*-
"""clase1_1_materia.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/CAUN94/tics100-2025/blob/main/clase1/clase1_1_materia.ipynb

# Bienvenida a la Programación con Python

## ¿Qué es Programar?

Programar es el proceso de diseñar y construir un programa ejecutable que realice una tarea específica o solucione un problema determinado. Es una habilidad esencial en el mundo moderno, que nos permite automatizar y mejorar procesos en casi todos los campos de estudio y trabajo.

## Introducción a Python

Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. Fue creado por Guido van Rossum y su primera versión fue lanzada en 1991. Vamos a utilizar Python 3.x.x en este curso, que es la versión más actual y soportada del lenguaje.

### Ventajas de Usar Python

1. **Facilidad de Aprendizaje**
   - Python es conocido por su sintaxis clara y legible, ideal para principiantes y usado ampliamente en la educación.

2. **Versatilidad**
   - Desde la automatización hasta el desarrollo de inteligencia artificial, Python se adapta a una amplia variedad de aplicaciones, siendo una herramienta valiosa para startups y grandes empresas por igual.

3. **Comunidad Activa**
   - Python cuenta con una comunidad global de desarrolladores que ofrece soporte, comparte recursos y facilita el aprendizaje continuo.

4. **Gran Biblioteca Estándar**
   - La extensa biblioteca estándar de Python incluye módulos para realizar una gran variedad de tareas, desde manejar protocolos de internet hasta crear interfaces gráficas.

5. **Ahorro Económico y de Tiempo**
   - Automatizar tareas repetitivas con Python puede ahorrar horas de trabajo manual y recursos económicos significativos.

6. **Gran Rendimiento**
   - Aunque Python no es el lenguaje más rápido en términos de tiempo de ejecución, su rendimiento es suficiente para la mayoría de las aplicaciones, permitiendo a los desarrolladores concentrarse en la solución de problemas más que en la optimización del código.

7. **Multiplataforma**
   - Python es compatible con los principales sistemas operativos, lo que permite ejecutar el mismo código en diferentes plataformas.

### ¿Qué se puede hacer con Python?

- **Desarrollo Web**: Creación de plataformas y aplicaciones web robustas.
- **Aprendizaje Automático**: Implementación de modelos que pueden aprender de los datos y hacer predicciones.
- **Desarrollo de Videojuegos**: Creación de juegos desde simples hasta complejos usando librerías como Pygame.
- **Automatización de Tareas**: Automatizar procesos de negocios y tareas diarias.
- **Extracción y Análisis Web**: Obtener datos de internet y analizarlos para obtener insights.
- **Desarrollo de Aplicaciones de Escritorio y Móviles**: Construir aplicaciones que los usuarios pueden instalar en sus dispositivos.
- **Ethical Hacking**: Testear y asegurar sistemas contra intrusiones.

## Tipos de Archivos en Python: .py vs .ipynb

En este curso, trabajaremos principalmente con dos tipos de archivos: `.py` y `.ipynb`. Cada uno tiene sus propias características y usos dentro del mundo de la programación en Python.

### Archivos .py

Los archivos con extensión `.py` son scripts de Python puros. Estos archivos contienen código que puede ser ejecutado por el intérprete de Python. Son ideales para la producción y el desarrollo de software en entornos profesionales. Puedes ejecutar estos scripts desde la línea de comando o mediante un IDE (Entorno de Desarrollo Integrado) como PyCharm, Visual Studio Code, o incluso desde un editor de texto simple.

**Ventajas de usar archivos .py:**
- **Estandarización**: Son el estándar en la industria para la distribución de código Python.
- **Automatización**: Fáciles de usar para la automatización de tareas ya que pueden ser ejecutados con un simple comando.
- **Integración**: Más sencillos de integrar con otros archivos y sistemas, especialmente en ambientes de desarrollo complejos.

Por ejemplo, el archivo `clase1_1_materia.py` contiene el mismo código que estamos viendo en este Jupyter, pero estructurado para ser ejecutado directamente por un intérprete de Python sin la necesidad de una interfaz gráfica.

### Archivos .ipynb (Jupyter Notebooks)

Lo que estamos usando ahora es un Jupyter Notebook, reconocible por la extensión `.ipynb`. Jupyter es una aplicación web que permite crear y compartir documentos que contienen código en vivo, ecuaciones, visualizaciones y texto narrativo. Son especialmente útiles en la educación, la ciencia de datos y en análisis donde la visualización de datos y la experimentación directa con el código son necesarias.

**Ventajas de usar Jupyter Notebooks:**
- **Interactividad**: Permiten modificar y ejecutar el código en bloques o celdas de manera interactiva.
- **Documentación**: Facilitan la documentación del código ya que permiten combinar código, texto explicativo y multimedia.
- **Compartir**: Son fáciles de compartir con otros, lo que los hace ideales para colaboraciones y educación.

### Conclusión

Dependiendo de tus necesidades, podrías elegir trabajar con uno u otro formato. En este curso, utilizaremos ambos: Jupyter Notebooks para la enseñanza y aprendizaje interactivo, y scripts `.py` para prácticas de programación más tradicionales y proyectos finales que requieran un entorno de ejecución estándar.

# Explorando el Comando `print` en Python

## ¿Por qué comenzamos con `print`?

Al aprender cualquier lenguaje de programación, el "Hello World" es el primer ejemplo clásico. Es un programa sencillo que muestra texto en la consola. Nos enseña cómo ejecutar un código básico y es perfecto para introducir el comando `print` en Python.

## Función del Comando `print`

El comando `print` en Python se utiliza para mostrar información en la pantalla. Es útil tanto para imprimir mensajes simples como para mostrar los resultados de operaciones aritméticas.

### Ejemplo Básico de Uso de `print`

```python
print('Hello World')  # Muestra "Hello World" en la pantalla
"""

# El Comando Print en Python
print('Hola Mundo')

"""# Importancia de las Comillas y Salto de Línea en `print`

## ¿Por qué el Texto debe Estar Entre Comillas?

En Python, el texto debe estar encerrado entre comillas (simples `'` o dobles `"`) para que sea reconocido como una cadena de caracteres o string. Las comillas le indican a Python que lo contenido dentro de ellas debe ser tratado como texto literal y no como código o nombre de variable.

### Ejemplo Básico

```python
print('Hola Mundo')
print('Hello World')
print('Hallo Welt')

"""

print('Hola Mundo')
print('Hello World')
print('Hallo Welt')

"""# Salto de Línea Automático en `print`

Aunque no lo veamos directamente, después de cada uso de `print`, Python añade un salto de línea. Esto significa que cada llamada a `print` comenzará en una nueva línea en la consola, lo cual organiza la salida y la hace más legible. Este comportamiento hace que los mensajes no se amontonen en una sola línea, facilitando la lectura de lo que se imprime.

# Errores Comunes al Usar Comillas

El uso incorrecto de las comillas puede llevar a varios errores en Python. A continuación, se muestran algunos ejemplos comunes de lo que podría salir mal cuando las comillas no se utilizan adecuadamente.

## Ejemplos de Errores

```python
# Error porque Python intenta interpretar 'Hola' y 'Mundo'
print(Hola Mundo)

# Error de sintaxis porque las comillas no están cerradas adecuadamente
print("Hola )

# Error similar al anterior, mezcla de comillas simples y dobles incorrectamente
print("Hola')

# Otro error de sintaxis por no cerrar las comillas correctamente
print("Hola)

"""

# print(Hola Mundo)

# print("Hola )

# print("Hola')

# print("Hola)

"""# `print` y Operaciones Aritméticas

`print` no solo es útil para mostrar texto, sino que también puede utilizarse para ejecutar y mostrar el resultado de operaciones aritméticas directamente.

## Ejemplos de Operaciones Aritméticas con `print`

En los siguientes ejemplos, utilizaremos `print` para realizar y mostrar diferentes operaciones aritméticas. Notarás que los números no llevan comillas, ya que queremos que Python los interprete como valores numéricos y no como texto.

```python
print(7+2)  # Suma, muestra 9
print(7-2)  # Resta, muestra 5
print(7*2)  # Multiplicación, muestra 14
print(7/2)  # División, muestra 3.5
print(7**2) # Potencia, muestra 49
print(7//2) # División entera, muestra 3

"""

print('7+2: ')
print(7+2)
print('7-2: ')
print(7-2)
print('7*2: ')
print(7*2)
print('7/2: ')
print(7/2)
print('7**2 (elevado): ')
print(7**2)
print('7//2 (división parte entera): ')
print(7//2)

"""# Interacción entre Texto y Números en Python

Es fundamental comprender cómo el texto y los números interactúan en `print`. Dependiendo de cómo se usen, Python puede interpretar y ejecutar las expresiones de diferentes maneras. Este conocimiento es crucial para evitar errores comunes y escribir programas efectivos.

## Ejemplos de Interacción entre Texto y Números

Observemos cómo Python maneja diferentes combinaciones de texto y números dentro de la función `print`.

```python
# Esto imprimirá exactamente el texto entre comillas
print("2+2")  # Muestra '2+2' como texto

# Concatenara '2+2' como texto
print("2"+"2")  # Muestra '2+2' como texto

# Esto calculará la suma antes de imprimir
print(2+2)  # Calcula 2+2 y muestra 4

"""

# Concatenara '2+2' como texto
print("2+2")  # Muestra '2+2' como texto

# Concatenara "2"+"2"" como texto
print("2"+"2")  # Muestra '22' como texto

# Esto producirá un error porque no se puede sumar un número a un string directamente
#  print("2"+2)  # TypeError: can only concatenate str (not "int") to str

# Esto repetirá el string '2' cuatro veces
print("2"*4)  # Muestra '2222'

"""# Personalización del Comportamiento de Salto de Línea en `print`

Uno de los comportamientos predeterminados de la función `print` en Python es añadir un salto de línea al final de cada mensaje. Esto significa que cada llamada a `print` terminará con un nuevo inicio de línea en la consola, separando la salida de diferentes llamadas a `print`. Sin embargo, este comportamiento se puede modificar según las necesidades del programa.

## Cómo `print` Maneja los Saltos de Línea por Defecto

Por defecto, `print` incluye el argumento `end='\n'`, que indica que después de imprimir el mensaje deseado, se debe añadir un salto de línea (`\n`). Este es un comportamiento útil para mantener la salida organizada y fácil de leer, especialmente cuando se imprimen múltiples líneas en secuencia.

## Modificar el Final de la Línea

Puedes cambiar este comportamiento predeterminado utilizando el argumento `end` en la función `print`. Al establecer un valor diferente para `end`, puedes decidir qué caracteres, si los hay, se imprimirán al final de la salida.

### Ejemplos de Modificación del Salto de Línea

```python
# Ejemplo de uso de print sin modificar el salto de línea
print('Hello, World!')
print('Continúa en una nueva línea')

# Ejemplo modificando el salto de línea para continuar en la misma línea
print('Hello, World!', end=' ')
print('Continúa en la misma línea')

# Ejemplo de eliminación del salto de línea
print('Hello, World!', end='')
print(' y no hay espacio entre estas frases.')

# Ejemplo de uso de un carácter diferente al final
print('Hello, World!', end='-')
print(' Estas frases están separadas por un guion.')

"""

# Ejemplo de uso de print sin modificar el salto de línea
print('Hello, World!')
print('Continúa en una nueva línea')
print() # Imprime una línea en blanco

# Ejemplo modificando el salto de línea para continuar en la misma línea
print('Hello, World!', end=' ')
print('Continúa en la misma línea')
print() # Imprime una línea en blanco

# Ejemplo de eliminación del salto de línea
print('Hello, World!', end='')
print(' y no hay espacio entre estas frases.')
print() # Imprime una línea en blanco

# Ejemplo de uso de un carácter diferente al final
print('Hello, World!', end='-')
print(' Estas frases están separadas por un guion.')

"""# Conclusión sobre el Comando `print`

Hemos completado nuestra exploración del comando `print` en Python. Ahora entiendes cómo utilizar esta función esencial para mostrar texto y resultados de cálculos en la consola. También has aprendido cómo manejar errores comunes, especialmente relacionados con la concatenación de texto y números, y cómo personalizar el salto de línea al final de tus mensajes de salida.

## Aplicación de lo Aprendido

Te animo a practicar lo que has aprendido utilizando `print` en diferentes contextos. Experimenta con la combinación de texto y números, y prueba diferentes valores para el argumento `end` para ver cómo afecta la presentación de tus programas. Estos ejercicios no solo reforzarán tu comprensión del material, sino que también mejorarán tu habilidad para depurar y mejorar la claridad de tus códigos.

"""

print('Mi primer Hola Mundo')

"""# Introducción al Comando `input`

Después de aprender cómo usar `print` para mostrar información, el siguiente paso es aprender a recibir información del usuario. Esto se hace mediante el comando `input`, que es esencial para interactuar con los usuarios en tiempo de ejecución de un programa.

## ¿Qué es `input`?

El comando `input` en Python permite a los usuarios ingresar datos que pueden ser utilizados por el programa. A diferencia de `print`, que envía datos a la salida estándar, `input` recibe datos desde la entrada estándar (por lo general, el teclado).

## Funcionamiento Básico de `input`

Cuando se ejecuta `input`, el programa se detiene y espera que el usuario escriba algo y presione Enter. Una vez que se presiona Enter, el programa continúa su ejecución. `input` siempre trata lo que recibe como una cadena de texto (string).

### Ejemplo Básico de Uso de `input`

```python
input('Por favor, introduce tu nombre: ')

"""

input('Escribe algo y presiona Enter: ')

print('Escribe otra cosa abajo')
input()

"""## Conclusiones

El comando input es una herramienta poderosa para hacer que tus programas sean interactivos. Permite a los usuarios proporcionar información en tiempo real, que puede ser esencial para la funcionalidad del programa. En las próximas secciones, aprenderemos cómo tomar esta entrada y usarla más efectivamente mediante la asignación a variables y otros métodos de procesamiento.
"""