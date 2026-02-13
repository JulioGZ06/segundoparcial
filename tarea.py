import os
os.system("cls")

print("=== CAPTURA DE ALUMNOS ===")

cantidad = int(input("¿Cuántos alumnos quieres capturar?: "))

# Lista donde guardaré todos los diccionarios
alumnos = []

for i in range(cantidad):
    print("\nAlumno", i+1)
    
    alumno = {}  # creo el diccionario vacío
    
    alumno["nombre"] = input("Nombre: ")
    alumno["edad"] = int(input("Edad: "))
    alumno["carrera"] = input("Carrera: ")
    
    # Agrego el diccionario a la lista
    alumnos.append(alumno)

print("\n=== MOSTRAR ALUMNOS ===")

for alumno in alumnos:
    print("\nAlumno guardado:")
    print("Nombre:", alumno["nombre"])
    print("Edad:", alumno.get("edad"))
    print("Carrera:", alumno["carrera"])
    
    # recorrer el diccionario
    print("Recorrer el diccionario:")
    for clave in alumno:
        print(clave, ":", alumno[clave])
    
    # funciones útiles
    print("Cantidad de datos:", len(alumno))
    print("Claves:", alumno.keys())
    print("Valores:", alumno.values())
    print("Pares clave-valor:", alumno.items())