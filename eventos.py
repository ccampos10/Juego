from entidades import Enemigo, Jugador
from pantalla import pantalla

class Evento:
    def __init__(self, nombreEvento:str, entidadesParticipe:dict) -> None:
        self.__nombreEvento = nombreEvento
        self.__entidadesParticipe = entidadesParticipe
        self.__comandos = []
    
    @property
    def nombre(self):
        return self.__nombreEvento
    
    @property
    def entidadesParticipe(self):
        return self.__entidadesParticipe
    
    @property
    def comandos(self):
        return self.__comandos
    
    @comandos.setter
    def comandos(self, value:list):
        if not (type(value) is list): raise ValueError("El valor no es del tipo 'list'")
        self.__comandos = value

class Pelea(Evento):
    def __init__(self, nombreEvento: str, entidadesParticipe: dict) -> None:
        super().__init__(nombreEvento, entidadesParticipe)
        super().comandos += 
    
    

class Evento:
    def __init__(self, nombreEvento, entidadesParticipe) -> None:
        self.__nombreEvento = nombreEvento
        self.__entidadesParticipe = entidadesParticipe
        self.__comandos = []
    
    @property
    def nombre(self):
        return self.__nombreEvento
    
    def danar(self, dano):
        self.__jugador.aplicarDano(dano)
    
    def iniciar(self):
        pantalla.notificacion("Esta es una funcion iniciar generica")

class Pelea(Evento):
    def __init__(self, nombre, jugador) -> None:
        super().__init__(nombre, jugador)
        self.__enemigo = None
    
    def generarEnegimo(self):
        ataques = [{'nombre': 'basico', 'dano': 10, 'energia': 0}]
        self.__enemigo = Enemigo('Zombie', 1, 1000, 10, 10, 1, ataques,1)
    
    def iniciar(self):
        if not self.__enemigo: self.generarEnegimo()
        pantalla.notificacion(f'Pelea iniciada con un {self.__enemigo.nombre}')
        
        def mostrarAtaques():
            pantalla.notificacion(f"Lista de ataques del jugador {self.jugador.nombre}")
            count = 0
            for ataque in self.jugador.ataques:
                count += 1
                pantalla.listar(f"{ataque['nombre']}: 'daño' {ataque['dano']}, 'energia' {ataque['energia']}", count)

        while self.__enemigo.estaVivo and self.jugador.estaVivo:
            mostrarAtaques()
            opcion = int(pantalla.cursor('Ingrese una opcion'))
            if opcion > self.jugador.ataques.__len__():
                print(f"La opcion '{opcion}' no se reconose, intentelo nuevamente")
            else:
                estaVivo = self.__enemigo.aplicarDano(self.jugador.ataques[opcion-1]['dano'])
                if not estaVivo:
                    pantalla.notificacion(f"El enemigo {self.__enemigo.nombre} esta muerto")
                    break
                estaVivo = self.jugador.aplicarDano(self.__enemigo.ataques[0]['dano'])
                if not estaVivo:
                    pantalla.notificacion(f"El jugador {self.jugador.nombre} esta muerto")
                    break

class Aventura(Evento):
    def __init__(self, nombre, jugador) -> None:
        super().__init__(nombre, jugador)
            