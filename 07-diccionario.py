""" 
que es un diccionario ?
es una estructura de datos que almacena en pares clave-valor

no se accede por posicion
"""
alumno={
    "nombre":"Ana",
    "edad":21,
    "carrera":"Ingenieria"
}
print(type(alumno))
print(alumno)

print(alumno["nombre"])
print(alumno.get("edad"))

alumno["promedio"]=9.2
print(alumno)
alumno["edad"]=22
print(alumno)
"""
eliminar par clave-valor
"""
del alumno["carrera"]
print(alumno)

#recorrer un diccionario
for clave in alumno:
    print(clave, ":",alumno[clave])
    
#funciones utiles para diccionarios
print("Cantidad de pares clave-valor: ",len(alumno))
print("Claves de diccionarios: ",alumno.keys())
print("Varoles del diccionario: ",alumno.values())
print("pares clave-valor: ",alumno.items())

