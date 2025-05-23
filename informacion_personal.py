# 1. Crear un diccionario con información inicial
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Mostrar el diccionario inicial
print("Diccionario inicial:")
print(informacion_personal)

# 2. Modificar el valor de "ciudad"
nueva_ciudad = input("\nPor favor ingrese una nueva ciudad: ")
informacion_personal["ciudad"] = nueva_ciudad

# 3. Agregar o actualizar la clave "profesion"
nueva_profesion = input("Por favor ingrese una nueva profesión: ")
informacion_personal["profesion"] = nueva_profesion

# 4. Verificar si la clave "telefono" existe y agregarla si no está
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = input("Por favor ingrese un número de teléfono: ")

# 5. Eliminar la clave "edad"
del informacion_personal["edad"]

# 6. Imprimir el diccionario final
print("\nDiccionario final:")
print(informacion_personal)
