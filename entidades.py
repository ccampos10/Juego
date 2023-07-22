class Entidad:
    """Base para todas las entidades del juego"""

    def __init__(self, nombre:str, nivel:int, vida:int, energia:int, danoBase:int, armadura:int, ataques:list, aguilidad:int) -> None:
        self.__nombre = nombre
        self.__nivel = nivel
        self.__vida = vida
        self.__energia = energia
        self.__danoBase = danoBase
        self.__armadura = armadura
        self.__eficienciaArmadura:int = 50 # Representado en %. Implementar que la armadura tiene distintos tipos de eficiencia dependiendo del tipo
        self.__ataques = ataques # Lista[{nombre,dano,energia que utiliza,probabilidad(en caso de que sea nesesario)}]
        self.__aguilidad = aguilidad
        self.__estaVivo = True
    
    @property
    def estaVivo(self) -> bool:
        """Consulta si la entidad sigue viva"""
        return self.__estaVivo
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def ataques(self):
        return self.__ataques
    
    @property
    def estados(self) -> dict:
        return {
            'Nombre': self.__nombre,
            'Nivel': self.__nivel,
            'Vida': self.__vida,
            'Energia': self.__energia,
            'Daño Base': self.__danoBase,
            'Armadura': self.__armadura,
            'Eficiencia de la armadura': self.__eficienciaArmadura,
            'Ataques': self.__ataques,
            'Aguilidad': self.__aguilidad,
        }
    
    def aplicarDano(self,dano):
        """Aplica un daño y retorna un boleano que indica si la entidad sigue viva o no"""
        #dano = int(dano/(int(self.__armadura*(self.__eficienciaArmadura/100))))
        self.__vida -= dano
        if self.__vida <= 0:
            self.__vida = 0
            self.__estaVivo = False
        return self.estaVivo
    
class Jugador(Entidad):
    def __init__(self, nombre:str, nivel:int, vida:int, energia:int, danoBase:int, armadura:int, ataques:list, aguilidad:int) -> None:
        super().__init__(nombre, nivel, vida, energia, danoBase, armadura, ataques, aguilidad)

class Enemigo(Entidad):
    def __init__(self, nombre:str, nivel:int, vida:int, energia:int, danoBase:int, armadura:int, ataques:list, aguilidad:int) -> None:
        super().__init__(nombre, nivel, vida, energia, danoBase, armadura, ataques, aguilidad)
