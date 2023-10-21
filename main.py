from pantalla import pantalla
from entorno import entorno

pantalla.notificacion("Bienbenido a mi juego")
entorno.generarJugador()

#pantalla.comandos = entorno.comandos # agregar los comandos de entorno
pantalla.ayuda()
comando = pantalla.cursor("Ingrese un comando")

while True:
    comando = comando.lower()
    if pantalla.comandos.__contains__(comando): # comando in pantalla.comandos
        pantalla.comandos[comando]()
    else: # cambiar por try except
        pantalla.notificacion(f"El comando '{comando}' no se reconose")
    comando = pantalla.cursor("Ingrese un comando")