class Personaje:
    def __init__(self, nombre: str) -> None:
        """
        Constructor de la clase Personaje.
        
        Parámetros:
            nombre (str): El nombre del personaje.
        """
        self.nombre = nombre  # Asigna el nombre del personaje
        self.nivel = 1  # Inicializa el nivel del personaje en 1
        self.experiencia = 0  # Inicializa la experiencia del personaje en 0

    def obtener_estado(self) -> None:
        """
        Método para imprimir el estado actual del personaje.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Nivel: {self.nivel}")
        print(f"Experiencia: {self.experiencia}")

    def asignar_estado(self, experiencia: int) -> None:
        """
        Método para asignar experiencia al personaje y actualizar su nivel si es necesario.
        
        Parámetros:
            experiencia (int): La cantidad de experiencia a asignar (positiva o negativa).
        """
        self.experiencia += experiencia  # Aumenta o disminuye la experiencia del personaje
        if self.experiencia >= 100:  # Si la experiencia alcanza o supera 100
            self.nivel += self.experiencia // 100  # Aumenta el nivel
            self.experiencia %= 100  # Actualiza la experiencia restante
        elif self.experiencia < 0 and self.nivel > 1:  # Si la experiencia es negativa y el nivel es mayor que 1
            self.nivel -= 1  # Reduce el nivel
            self.experiencia += 100  # Ajusta la experiencia restante

    def __lt__(self, otro_personaje: 'Personaje') -> bool:
        """
        Método de comparación menor que (<) entre personajes basado en sus niveles.
        """
        return self.nivel < otro_personaje.nivel

    def __gt__(self, otro_personaje: 'Personaje') -> bool:
        """
        Método de comparación mayor que (>) entre personajes basado en sus niveles.
        """
        return self.nivel > otro_personaje.nivel

    @staticmethod
    def calcular_probabilidad(personaje1: 'Personaje', personaje2: 'Personaje') -> float:
        """
        Método estático para calcular la probabilidad de ganar un enfrentamiento con otro personaje.
        """
        if personaje1 < personaje2:  # Si el nivel del primer personaje es menor que el del segundo
            return 0.33  # Retorna una probabilidad baja
        elif personaje1 > personaje2:  # Si el nivel del primer personaje es mayor que el del segundo
            return 0.66  # Retorna una probabilidad alta
        else:  # Si ambos personajes tienen el mismo nivel
            return 0.5  # Retorna una probabilidad media

    @staticmethod
    def enfrentamiento_con_orco(personaje: 'Personaje', probabilidad: float) -> int:
        """
        Método estático que simula un enfrentamiento con un orco y devuelve la opción elegida por el jugador.
        """
        print("Ha aparecido un orco!")
        print(f"Probabilidad de ganar: {probabilidad * 100}%")
        print("Si ganas, recibirás 50 puntos de experiencia. Si pierdes, perderás 30 puntos de experiencia.")
        opcion = int(input("¿Deseas atacar (1) o huir (2)? "))  # Solicita al jugador que elija entre atacar o huir
        return opcion  # Devuelve la opción elegida por el jugador
