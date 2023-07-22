class Pantalla:
    def __init__(self):
        self.__listaComandos = [
            ['ayuda','Muestra este mensaje', self.ayuda],
            ['salir','Finaliza el juego', self.salir],
        ]
    
    @property
    def comandos(self):
        """Retorna una lista con todos los comandos admitidos y su ejecutable"""
        return {e[0]: e[2] for e in self.__listaComandos}
    
    @comandos.setter
    def comandos(self, dato):
        self.__listaComandos = [*dato, *self.__listaComandos]
    
    def cursor(self, mensaje:str = '') -> str:
        if mensaje != '':
            print(mensaje)
        return input('-> ')
    
    def div(self, esPrimero, cant = 50):
        if esPrimero:
            print("\n"+('-'*cant))
        else:
            print(('-'*cant)+'\n')
    
    def notificacion(self, mensaje:str):
        self.div(True, mensaje.__len__())
        print(mensaje)
        self.div(False, mensaje.__len__())
    
    def listar(self, mensaje:str, num:int = None, sangria:str = "  "):
        pre:str = ''
        if num:
            pre = f'{num}.- '
        print(sangria,pre,mensaje,sep='')
    
    def ayuda(self):
        self.notificacion("Comandos admitidos")
        [self.listar(e[0]+' -> '+e[1]) for e in self.__listaComandos]
        self.div(False)
    
    def salir(self):
        exit()
        
pantalla = Pantalla()