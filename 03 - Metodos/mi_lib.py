class Operaciones:
    def __init__(self) -> None:
        pass

    @staticmethod
    def suma(lista, num = None):
        if num:
            result = []
            for element in lista:
                result.append(element + num)
        else:
            result = 0
            for element in lista:
                result = result + element
        return result

