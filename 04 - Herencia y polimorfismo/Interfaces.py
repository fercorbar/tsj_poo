from abc import ABC, abstractmethod

class ControlRemoto(ABC):
    @abstractmethod
    def siguiente_canal(self):
        pass

    @abstractmethod
    def canal_anterior(self):
        pass

    @abstractmethod
    def subir_volumen(self):
        pass

    @abstractmethod
    def bajar_volumen(self):
        pass

class ControlSamsung(ControlRemoto):
    def siguiente_canal(self):
        print("Samsung -> Siguiente")

    # def canal_anterior(self):
    #     print("Samsung -> Anterior")

    # def subir_volumen(self):
    #     print("Samsung -> Subir")

    # def bajar_volumen(self):
    #     print("Samsung -> Bajar")

class ControlLG(ControlRemoto):
    def siguiente_canal(self):
        print("LG -> Siguiente")
    
    # def canal_anterior(self):
    #     print("LG -> Anterior")

    # def subir_volumen(self):
    #     print("LG -> Subir")

    # def bajar_volumen(self):
    #     print("LG -> Bajar")

# Creación de instancias
samsung_control = ControlSamsung()
lg_control = ControlLG()

samsung_control.siguiente_canal()  # Salida: Samsung -> Siguiente
lg_control.siguiente_canal()       # Salida: LG -> Siguiente
