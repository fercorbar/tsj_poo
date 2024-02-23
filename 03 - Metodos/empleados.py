from empleadoslib import *

nose_chon = Empresa("No sé CHON") # Creación de empresa

# Creación de empleados
fer = EmpleadoIndefinido("Fernando", 37, 378111111, "M", 1000)
jp = EmpleadoIndefinido("Juan Pablo", 19, 378111111, "M", 2000)
gael = EmpleadoIndefinido("gael", 19, 378111111, "M", 1000)
pablo = EmpleadoIndefinido("pablo", 19, 378111111, "M", 1000)
orlando = EmpleadoIndefinido("orlando", 19, 378111111, "M", 1000)
onix = EmpleadoIndefinido("onix", 19, 378111111, "M", 1000)

nose_chon.visualizar_empleados()

# Contrataciones
# nose_chon.contratar(fer)
# nose_chon.contratar(jp)
# nose_chon.contratar(gael)
# nose_chon.contratar(pablo)
# nose_chon.contratar(orlando)
# nose_chon.contratar(onix)

nose_chon.contratar(fer)
nose_chon.visualizar_empleados()
nose_chon.contratar([fer, jp, gael, pablo, orlando, onix], multiple=True)

nose_chon.visualizar_empleados()
nose_chon.despedir("gael")
nose_chon.visualizar_empleados()

nose_chon.buscar_empleado("onix")
print("---------------------------------")
# nose_chon.visualizar_empleados(compacto=False)

print(jp.calcular_aumento(20))


