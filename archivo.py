# Creamos y abrimos el archivo
archivo = open("my_notes.txt", "w")

# Escribimos notas
archivo.write("Lunes: Comenzar la semana con buena energía.\n")
archivo.write("Martes: Revisar el material de clase y practicar ejercicios.\n")
archivo.write("Miércoles: Asistir al taller de programación avanzada.\n")
archivo.write("Jueves: Organizar apuntes y resolver dudas pendientes.\n")
archivo.write("Viernes: Preparar el resumen para el examen final.\n")

# Cerramos el archivo para guardar los cambios
archivo.close()

# Abrimos el archivo
archivo = open("my_notes.txt", "r")

# Leemos y mostramos cada línea una por una
print("Contenido del archivo generado:")
linea = archivo.readline()
while linea:
    print(linea.strip())
    linea = archivo.readline()


# Cerramos el archivo después de la lectura
archivo.close()
