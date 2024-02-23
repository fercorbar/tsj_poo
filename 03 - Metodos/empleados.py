from empleadoslib import *


nose_chon = Empresa("No sé CHON")
fer = EmpleadoIndefinido("Fernando", 37, 378111111, "M", 1000)
jp = EmpleadoIndefinido("Juan Pablo", 19, 378111111, "M", 1000)
gael = EmpleadoIndefinido("gael", 19, 378111111, "M", 1000)
pablo = EmpleadoIndefinido("pablo", 19, 378111111, "M", 1000)
orlando = EmpleadoIndefinido("orlando", 19, 378111111, "M", 1000)
onix = EmpleadoIndefinido("onix", 19, 378111111, "M", 1000)
nose_chon.visualizar_empleados()

nose_chon.contratar(fer)
nose_chon.contratar(jp)
nose_chon.contratar(gael)
nose_chon.contratar(pablo)
nose_chon.contratar(orlando)
nose_chon.contratar(onix)
nose_chon.visualizar_empleados()



