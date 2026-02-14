import os
os.system("cls")

alumnos = []

while True:
    try:
        num = int(input("cuantos alumnos quieres ingresar? "))
        break
    except ValueError:
        print("Error: Por favor ingrese un numero valido.")
        
for i in range(num):
    print("\nAlumno " + str(i + 1)) #sin el str me da error porque texto y numeros no se unen
    edad = input("Ingresa la edad: ")
    nombre = input("Ingresa el nombre: ")
    materia = input("Ingresa la materia: ")
    calificacion = int(input("Ingresa la calificacion: "))
    
alumno = {
        "nombre": nombre,
        "edad": edad,
        "materia": materia,
        "calificacion": calificacion    
    }

alumnos.append(alumno)

os.system ("cls")

if alumnos:
    total_calificaciones = sum(alumnos["calificacion"] for alumno in alumnos)
    promedio = total_calificaciones/ len(alumnos)
    print(f"promedio de calificaiones: {promedio}")
else:
    print("No se ingresaron las calificaciones.")
    
print("Lista completa de alumnos ")
for alumno in alumnos:
    print(alumno)
