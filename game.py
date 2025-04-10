from juego import PiedraPapelTijera

def mostrar_eleccion(eleccion):
    """Muestra la elección del jugador o la computadora de forma visual"""
    if eleccion == 'piedra':
        return """
       _______
      |       |
      | Piedra|
      |_______|
        """
    elif eleccion == 'papel':
        return """
       _______
      |       |
      | Papel |
      |_______|
        """
    elif eleccion == 'tijera':
        return """
       _______
      |       |
      |Tijera |
      |_______|
        """

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
        print(f"\nTu elección:\n{mostrar_eleccion(jugador)}")
        print(f"La computadora eligió:\n{mostrar_eleccion(computadora)}")
        
        resultado = juego.determinar_ganador(jugador, computadora)
        print(f"\n{resultado}")
        
        # Mostrar puntos y victorias después de cada ronda
        print(juego.mostrar_puntos())
        print(juego.mostrar_victorias())
        
        otra_vuelta = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
        
        if otra_vuelta == 's':
            continuar = input("¿Quieres reiniciar el juego? (s/n): ").lower()
            if continuar == 's':
                juego = PiedraPapelTijera()  # Reinicia el juego
                print("\nEl juego ha sido reiniciado.\n")
                continue
        else:
            print("Gracias por jugar!")
            break

if __name__ == "__main__":
    jugar()
