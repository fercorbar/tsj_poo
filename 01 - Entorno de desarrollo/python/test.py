misael = {
    "nombre": "Misael",
    "edad": 18,
    "calificacion": 120
}
jp = {
    "nombre": "Juan Pablo",
    "edad": 19,
    "calificacion": 140
}

alumnos = [misael, jp]
for alumno in alumnos:
    descripcion = f"{alumno['nombre']} tiene {alumno['edad']} años y va a sacar {alumno['calificacion']}"
    print(descripcion)

i = 0
while i < 5:
    print(i)
    i += 1
