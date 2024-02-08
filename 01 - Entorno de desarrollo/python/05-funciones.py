# Funciones
# Las funciones son bloques de código que se pueden llamar
# para realizar una tarea específica.

# Las funciones se definen con la palabra clave def seguida del nombre de la 
# función y paréntesis.
def saludar():
    print("Hola!")
# Para llamar a una función se escribe el nombre de la función seguido de paréntesis.
saludar()

# Las funciones pueden recibir parámetros.
def saludar(nombre):
    print(f"Hola {nombre}!")
saludar("Juan")

# Las funciones pueden retornar valores.
def sumar(a, b):
    return a + b
resultado = sumar(3, 2)
print(resultado)

# Las funciones pueden recibir parámetros con valores por defecto.
def saludar(nombre="Mundo"):
    print(f"Hola {nombre}!")
saludar()
saludar("Juan")

# Las funciones pueden retornar múltiples valores.
def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division