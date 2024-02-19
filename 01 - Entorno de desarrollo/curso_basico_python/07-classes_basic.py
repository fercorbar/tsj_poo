class NombreDeMiClase:
    def __init__(self, atributo_1, atributo_2):
        # Dentro de paréntesis se coloca la referencia a la instancia y los argumentos necesarios para la creación de la misma
        print("Constructor")
        self.atributo_1 = atributo_1  # self hace referencia a la instancia de la clase
        self.atributo_2 = atributo_2

    def metodo_1(self):
        print(f"Hola, el valor de attr1 es: {self.atributo_1} y el valor de attr2 es: {self.atributo_2}");

    def __del__(self):
        print('Destructor')

mi_objeto = NombreDeMiClase("Valor atributo_1", "Valor atributo_1") # En esta línea se instancia la clase
mi_objeto.metodo_1() 


