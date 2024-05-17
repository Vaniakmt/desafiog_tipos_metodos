from personaje import Personaje  # Importar la clase Personaje desde el módulo personaje
import random  # Importar el módulo random para generar números aleatorios

class Juego:  # Definir la clase Juego
    def __init__(self) -> None:  # Método inicializador de la clase
        pass  # No hace nada en el inicializador

    def iniciar_juego(self) -> None:  # Método para iniciar el juego
        print("¡Bienvenido a Gran Fantasía!")  # Mensaje de bienvenida al juego
        nombre_personaje = input("Por favor indique nombre de su personaje: ")  # Solicitar al usuario el nombre del personaje
        
        # Crear personaje del jugador con el nombre ingresado
        jugador = Personaje(nombre_personaje)
        # Imprimir estado inicial del jugador
        print(f"NOMBRE: {jugador.nombre} NIVEL: {jugador.nivel} EXP: {jugador.experiencia}")

        # Crear personaje del orco con nombre predeterminado "Orco"
        orco = Personaje("Orco")
        # Imprimir mensaje de aparición del orco
        print("¡Oh no!, ¡Ha aparecido un Orco!")

        while True:  # Bucle principal del juego
            # Calcular probabilidad de ganar el enfrentamiento con el orco
            probabilidad_ganar = Personaje.calcular_probabilidad(jugador, orco)
            # Imprimir la probabilidad de ganar el enfrentamiento
            print(f"Con tu nivel actual, tienes {probabilidad_ganar * 100:.1f}% de probabilidades de ganarle al Orco.")
            print("Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.")
            print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
            print("¿Qué deseas hacer?")
            print("1. Atacar")
            print("2. Huir")

            opcion = int(input())  # Obtener la opción seleccionada por el usuario

            if opcion == 1:  # Si el jugador elige atacar
                resultado = random.uniform(0, 1)  # Generar un número aleatorio entre 0 y 1
                if resultado <= probabilidad_ganar:  # Si el resultado es menor o igual a la probabilidad de ganar
                    print("¡Le has ganado al orco, felicidades!")
                    print("¡Recibirás 50 puntos de experiencia!")
                    jugador.asignar_estado(50)  # Aumentar la experiencia del jugador en 50 puntos
                    orco.asignar_estado(-30)  # Reducir la experiencia del orco en 30 puntos
                    if orco.experiencia < 0:  # Si la experiencia del orco es negativa
                        orco.asignar_estado(-orco.experiencia)  # Ajustar la experiencia del orco a cero
                else:  # Si el resultado es mayor que la probabilidad de ganar
                    print("¡Oh no! ¡El orco te ha ganado!")
                    print("¡Has perdido 30 puntos de experiencia!")
                    jugador.asignar_estado(-30)  # Reducir la experiencia del jugador en 30 puntos
                    if jugador.experiencia < 0:  # Si la experiencia del jugador es negativa
                        jugador.asignar_estado(-jugador.experiencia)  # Ajustar la experiencia del jugador a cero
                    orco.asignar_estado(50)  # Aumentar la experiencia del orco en 50 puntos
                    if orco.experiencia < 0:  # Si la experiencia del orco es negativa
                        orco.asignar_estado(-orco.experiencia)  # Ajustar la experiencia del orco a cero
                # Imprimir estado actualizado del jugador y del orco
                print(f"NOMBRE: {jugador.nombre} NIVEL: {jugador.nivel} EXP: {jugador.experiencia}")
                print(f"NOMBRE: {orco.nombre} NIVEL: {orco.nivel} EXP: {max(0, orco.experiencia)}")

            elif opcion == 2:  # Si el jugador elige huir
                print("¡Has huido! El orco ha quedado atrás.")
                break  # Salir del bucle y terminar el juego

# Llamada para iniciar el juego
Juego().iniciar_juego()
