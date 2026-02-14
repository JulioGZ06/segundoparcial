import os
os.system("cls")

print("=== CAPTURA DE ALUMNOS ===")

cantidad = int(input("¿Cuántos alumnos quieres capturar?: "))

alumnos = []

for i in range(cantidad):
    print("\nAlumno", i+1)
    
    alumno = {}
    
    alumno["nombre"] = input("Nombre: ")
    alumno["edad"] = int(input("Edad: "))
    alumno["materia"] = input("Materia: ")
    alumno["calificacion"] = float(input("Calificación: "))
    
    alumnos.append(alumno)

print("\n=== MOSTRAR ALUMNOS ===")

for alumno in alumnos:
    print("\nNombre:", alumno["nombre"])
    print("Edad:", alumno["edad"])
    print("Materia:", alumno["materia"])
    print("Calificación:", alumno["calificacion"])

print("====lista de alumnos====")
for alumno in alumnos:
    print(alumno)



suma = 0
for alumno in alumnos:
    suma += alumno["calificacion"]

if len(alumnos) > 0:
    promedio = suma / len(alumnos)
else:
    promedio = 0


grupo = {
    "alumnos_registrados": len(alumnos),
    "promedio_calificaciones": promedio
}

print("\n=== RESUMEN DEL GRUPO ===")
print("Alumnos registrados:", grupo["alumnos_registrados"])
print("Promedio:", grupo["promedio_calificaciones"])