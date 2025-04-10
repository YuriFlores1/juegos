from juego import PiedraPapelTijera

def jugar():
    juego = PiedraPapelTijera()
    
    print("¡Bienvenido al juego Piedra, Papel o Tijera!")
    print("Elige entre 'piedra', 'papel' o 'tijera'.")

    while True:
        jugador = input("Tu elección: ").lower()
        
        if jugador not in ['piedra', 'papel', 'tijera']:
            print("Elección no válida. Por favor, elige entre 'piedra', 'papel' o 'tijera'.")
            continue

        computadora = juego.obtener_eleccion_computadora()
        print(f"La computadora eligió: {computadora}")
        
        resultado = juego.determinar_ganador(jugador, computadora)
        print(resultado)
        
        otra_vuelta = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if otra_vuelta != 's':
            break

if __name__ == "__main__":
    jugar()
