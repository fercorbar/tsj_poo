# Condicionales

# if
if True:
    print("Es verdadero")

# if else
if False:
    print("Es verdadero")
else:
    print("Es falso")

# if elif else
if False:
    print("Es verdadero")
elif True:
    print("Es verdadero")
else:    
    print("Es falso")


# match case
var = 2
match var:
    case 1:
        print("Es 1")
    case 2:
        print("Es 2")
    case 3:
        print("Es 3")
    case _:
        print("No es ninguno de los anteriores")
