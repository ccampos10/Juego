from pantalla import pantalla
from entidades import Jugador, Enemigo
from eventos import Pelea

class Entorno:
    def __init__(self):
        self.__comandos = [
            ['estados','Muestra los estados del jugador', self.estados],
            ['avanzar', 'Avanza en la masmora, generando un nuevo evento', self.generarEvento],
        ]
        self.__jugador:Jugador = None
    
    def generarJugador(self):
        """Genera un jugador"""
        nombre = pantalla.cursor("Ingrese el nombre del jugador")
        ataques=[{'nombre': 'basico', 'dano': 10, 'energia': 0}, {'nombre': 'fuerte', 'dano': 15, 'energia': 10}]
        self.__jugador = Jugador(nombre, 1, 1000, 10, 10, 1, ataques, 1)
    
    @property
    def comandos(self):
        return self.__comandos
    
    @property
    def jugador(self) -> Jugador:
        return self.__jugador
    
    @property
    def estadosJugador(self) -> dict:
        return self.__jugador.estados
    
    def generarEvento(self):
        evento = Pelea('pelea',self.__jugador)
        evento.iniciar()
        if not self.jugador.estaVivo:
            pantalla.notificacion("Juego terminado")
            pantalla.salir()
    
    def estados(self):
        pantalla.notificacion(f"Estados del jugador {self.estadosJugador['Nombre']}")
        for estado in self.estadosJugador:
            if estado == 'Ataques':
                pantalla.listar(estado+':')
                cont = 0
                for ataque in self.estadosJugador[estado]:
                    cont += 1
                    text = ''
                    for parametro in ataque:
                        if text != '': text += ', '
                        text += parametro+': '+str(ataque[parametro])
                    pantalla.listar(text,cont,'    ')
            else:
                pantalla.listar(estado + ' -> ' + str(self.estadosJugador[estado]))
        #[self.listar(e + ' -> ' + entorno.estadosJugador[e]) for e in entorno.estadosJugador]
        pantalla.div(False)
    

entorno = Entorno()