import random

class PiedraPapelTijera:
    def __init__(self):
        self.opciones = ['piedra', 'papel', 'tijera']
    
    def obtener_eleccion_computadora(self):
        return random.choice(self.opciones)
    
    def determinar_ganador(self, jugador, computadora):
        if jugador == computadora:
            return "Es un empate."
        elif (jugador == 'piedra' and computadora == 'tijera') or \
             (jugador == 'papel' and computadora == 'piedra') or \
             (jugador == 'tijera' and computadora == 'papel'):
            return "¡Ganaste!"
        else:
            return "La computadora ganó."

