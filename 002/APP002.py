# app002.py
# Programa de ejemplo: Variables y tipos de datos en python
# Autor: Mario Gabriel Martinez Garduño
# Grupo: 6010

# Declaracion de variables de diferentes tipos
edad = 19                # int (entero) 🫠
altura = 1.85            # float (decimal) 🫠
nombre = "Mario"         # str (cadena de texto) 🫠
es_estudiante = True     # bool (booleano) 🫠
materias = ["Matematicas", "Ingles", "Informatica", "Quimica", "Administracion", "Fisica"]  # list (lista) 🫠

# Mostrar los valores y tipos de cada variable
print("📋 Información del usuario:")
print(f"Nombre: {nombre} ▶️ (tipo: {type(nombre)})")
print(f"Edad: {edad} ▶️ (tipo: {type(edad)})")
print(f"Altura: {altura} ▶️ (tipo: {type(altura)})")
print(f"¿Es estudiante?: {es_estudiante} ▶️ (tipo: {type(es_estudiante)})")
print(f"Materias: {materias} ▶️ (tipo: {type(materias)})")
print("-" * 40)

# Solicitar datos al usuario
ciudad = input("🏙️ Ingresa tu ciudad: ")
calificacion = float(input("📏 Ingresa tu calificación promedio: "))

# Mostrar los datos ingresados
print(f"Ciudad: {ciudad} ▶️ (tipo: {type(ciudad)})")
print(f"Calificación promedio: {calificacion} ▶️ (tipo: {type(calificacion)})")
print("-" * 40)

# Operaciones con variables
# 1. Suma de enteros
nueva_edad = edad + 1
print(f"El próximo año tendrás {nueva_edad} años 🎉")

# 2. Concatenación de cadenas
presentacion = nombre + " vive en " + ciudad
print(f"Presentación: {presentacion} 🗣️")

# 3. Agregar un elemento a la lista
materias.append("Programación")
print(f"Materias actualizadas: {materias} =📘")

print("-" * 40)

# Explicación final sobre los tipos de datos
# Los tipos de datos son importantes porque determinan qué operaciones se pueden realizar con cada variable.
# Por ejemplo, no se puede sumar un número y una cadena de texto directamente.
# Usar correctamente los tipos de datos ayuda a evitar errores y a que el programa funcione correctamente.

print("✅ ¡Fin del programa! Recuerda que los tipos de datos son la base de la programación en Python. 🧠")