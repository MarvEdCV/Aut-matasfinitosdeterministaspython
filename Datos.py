class datosAFD:

    def __init__(self,nombre,estados,alfabeto,estadoInicial,estadoAceptacion,Transicioness):
        self.nombre = nombre
        self.estados = estados
        self.alfabeto = alfabeto
        self.EstadoInicial = estadoInicial
        self.EstadoAceptacion = estadoAceptacion
        self.Transicioness = Transicioness

class transiciones:
    def __init__(self, inicio, dato, final):
        self.inicio=inicio
        self.dato=dato
        self.final=final
