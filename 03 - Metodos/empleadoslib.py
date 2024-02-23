import math

class Empleado:
    def __init__(self, nombre, edad, telefono, genero):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.genero = genero

    def info(self):
        return f"{self.nombre}, edad: {self.edad}, gen: {self.genero}, tel: {self.telefono}"

class EmpleadoTemporal(Empleado):
    def __init__(self, nombre, edad, telefono, genero, fecha_termino):
        self.fecha_termino = fecha_termino
        super(EmpleadoTemporal, self).__init__(nombre, edad, telefono, genero)

class EmpleadoIndefinido(Empleado):
    def __init__(self, nombre, edad, telefono, genero, salario):
        self.salario = salario
        super(EmpleadoIndefinido, self).__init__(nombre, edad, telefono, genero)
    
    def calcular_aumento(self, porcentaje):
        return self.salario * (porcentaje/100)

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__empleados = []

    # def __contratar_uno(self, empleado):
    #     empleado_ya_esta_registrado = False
    #     for empleado_registrado in self.__empleados:
    #         if empleado_registrado.nombre == empleado.nombre:
    #             empleado_ya_esta_registrado = True
    #     if not empleado_ya_esta_registrado:
    #         self.__empleados.append(empleado)


    # def contratar(self, personas_a_contratar, multiple = False):
    #     if multiple:
    #         for persona in personas_a_contratar:
    #             self.__contratar_uno(persona)
    #     else:
    #         self.__contratar_uno(personas_a_contratar)


    def contratar(self, personas_a_contratar, multiple = False):
        if multiple:
            aux = personas_a_contratar
        else:
            aux = [personas_a_contratar]
        for persona in aux:
            empleado_ya_esta_registrado = False
            for empleado_registrado in self.__empleados:
                if empleado_registrado.nombre == persona.nombre:
                    empleado_ya_esta_registrado = True
            if not empleado_ya_esta_registrado:
                self.__empleados.append(persona)



    def despedir(self, nombre_empleado):
        for empleado in self.__empleados:
            if empleado.nombre == nombre_empleado:
                self.__empleados.remove(empleado)
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
                    print(empleado.info())

    def buscar_empleado(self, texto_busqueda):
        for empleado in self.__empleados:
            if texto_busqueda in empleado.nombre:
                print(empleado.info())
                break

    