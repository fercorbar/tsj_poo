import math

class Empleado:
    def __init__(self, nombre, edad, telefono, genero):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.genero = genero

class EmpleadoTemporal(Empleado):
    def __init__(self, nombre, edad, telefono, genero, fecha_termino):
        self.fecha_termino = fecha_termino
        super(EmpleadoTemporal, self).__init__(nombre, edad, telefono, genero)

class EmpleadoIndefinido(Empleado):
    def __init__(self, nombre, edad, telefono, genero, salario):
        self.salario = salario
        super(EmpleadoIndefinido, self).__init__(nombre, edad, telefono, genero)
    
    def calcular_aumento(self, porcentaje):
        return math.round(self.salario * (porcentaje/100),2)

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__empleados = []

    def contratar(self, empleado):
        empleado_ya_esta_registrado = False
        for empleado_registrado in self.__empleados:
            if empleado_registrado.nombre == empleado.nombre:
                empleado_ya_esta_registrado = True
        if not empleado_ya_esta_registrado:
            self.__empleados.append(empleado)
            # print(f"{empleado.nombre}, bienvenido a tu empresa {self.nombre}")
        # else:
        #     print(f"El empleado {empleado.nombre} no se puede contratar ya se encuentra contratado")

    def despedir(self, nombre_empleado):
        for empleado in self.__empleados:
            if empleado == nombre_empleado:
                self.__empleados.pop(empleado)
                break

    def visualizar_empleados(self, compacto = True):
        if compacto:
            result = ""
            for empleado in self.__empleados:
                if result == "":
                    result += f"{empleado.nombre}"
                else:
                    result += f", {empleado.nombre}"
            print(result)
        else:
            if len(self.__empleados) == 0:
                print("No hay empleados")
            else:
                for empleado in self.__empleados:
                    print(f"{empleado.nombre} Edad: {empleado.edad}, Género {empleado.genero}, Tel: {empleado.telefono}")

    

    