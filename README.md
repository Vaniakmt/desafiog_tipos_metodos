
# Desafío - Tipos de métodos

## Descripcion del proyecto

Has sido contratado por la startup “Juegos por comida”, y se te ha solicitado desarrollar el
algoritmo de la primera escena de su próximo juego “Gran Fantasía”.
El prototipo debe desarrollarse utilizando una aplicación de consola escrita en Python, que
conste de un script principal que ejecute el juego, y una clase que permita crear personajes,
que debe ser importada en el script principal. Las opciones de juego del usuario, así como el
nombre de su personaje, se deben solicitar mediante input.


## Requerimientos
1. En un archivo llamado personaje.py, crea la clase que permita crear personajes. Considerando la información entregada en la descripción del problema, la clase debetener los siguientes métodos:

- Constructor (considera parámetros y valores asignados a atributos de instancia)
- Getter de estado.
- Setter de estado.
- Sobrecarga para comparar “menor que” .
- Sobrecarga para comparar “mayor que”.
- Sobrecarga para comparar “igual que” (opcional).
- Método de instancia que retorna la probabilidad de la instancia actual deganar respecto de otra instancia (opcional).
- Método que muestra diálogo de enfrentamiento al orco (incluyendo probabilidad de ganar) y retorna opción escogida por el jugador (opcional).

- En el mismo archivo, manejar las posibles excepciones al leer cada línea y/o generar cada instancia, y agregar la excepción en un archivo error.log

2. En archivo llamado juego.py, crea la clase que permita jugar, considerando la información entregada en la descripción del problema:
- Importar módulos necesarios para el desarrollo del juego.
- Creación de personajes y almacenamiento de opción de juego del jugador (calculando y mostrando probabilidad de ganar)
- Para la opción de ataque, según el resultado obtenido, actualización de estados de los personajes.
- A continuación del punto anterior, dentro del ataque, mostrar estados actualizados de los personajes, y nueva consulta al usuario considerando la probabilidad actualizada de ganar.

## Instalacion

Requisitos previos
- Python >= 3.x
- Pip (administrador de paquetes de Python)
## Pasos de instalación
- Clona este repositorio en tu máquina local:
```bash
    git clone https://github.com/Vaniakmt/desafiog_tipos_metodos.git

```
