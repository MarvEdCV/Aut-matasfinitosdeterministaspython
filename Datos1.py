class DatosGR:
    def __init__(self,nombre1, nTerminales, terminales, nTerminalInicial,Producciones):
        self.nombre1 = nombre1
        self.nTerminales = nTerminales
        self.terminales = terminales
        self.nTerminalInicial = nTerminalInicial
        self.Producciones = Producciones
class producciones:
    def __init__(self, inicio,final):
        self.inicio = inicio
        self.final = final