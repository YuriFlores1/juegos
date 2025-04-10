import random

class PiedraPapelTijera:
    def __init__(self):
        self.opciones = ['piedra', 'papel', 'tijera']
        self.puntos_jugador = 0
        self.puntos_computadora = 0
        self.victorias_jugador = 0
        self.victorias_computadora = 0
    
    def obtener_eleccion_computadora(self):
        return random.choice(self.opciones)
    
    def determinar_ganador(self, jugador, computadora):
        if jugador == computadora:
            self.puntos_jugador += 5
            self.puntos_computadora += 5
            return "Es un empate."
        elif (jugador == 'piedra' and computadora == 'tijera') or \
             (jugador == 'papel' and computadora == 'piedra') or \
             (jugador == 'tijera' and computadora == 'papel'):
            self.victorias_jugador += 1
            self.puntos_jugador += 10
            return "¡Ganaste!"
        else:
            self.victorias_computadora += 1
            self.puntos_computadora += 10
            return "La computadora ganó."
    
    def mostrar_puntos(self):
        return f"Puntos - Jugador: {self.puntos_jugador} | Computadora: {self.puntos_computadora}"
    
    def mostrar_victorias(self):
        return f"Victorias - Jugador: {self.victorias_jugador} | Computadora: {self.victorias_computadora}"
