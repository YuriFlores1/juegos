import random

class PiedraPapelTijera:
    def __init__(self):
        self.opciones = ['piedra', 'papel', 'tijera']
        self.puntos_jugador = 0
        self.puntos_computadora = 0
    
    def obtener_eleccion_computadora(self):
        return random.choice(self.opciones)
    
    def determinar_ganador(self, jugador, computadora):
        if jugador == computadora:
            return "Es un empate."
        elif (jugador == 'piedra' and computadora == 'tijera') or \
             (jugador == 'papel' and computadora == 'piedra') or \
             (jugador == 'tijera' and computadora == 'papel'):
            self.puntos_jugador += 1
            return "¡Ganaste!"
        else:
            self.puntos_computadora += 1
            return "La computadora ganó."
    
    def mostrar_puntos(self):
        return f"Jugador: {self.puntos_jugador} | Computadora: {self.puntos_computadora}"
