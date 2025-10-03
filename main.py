import random
import arcade

# tile es el tamaño en pixeles de cada cuadrito del tablero
TILE = 20
# número de columnas y de filas
COLS, ROWS = 32, 24
# definir el ancho y el alto del juego
WIDTH, HEIGHT = COLS * TILE, ROWS * TILE
# color de backgroud
BG = arcade.color.DARK_SLATE_GRAY

MOVE_EVERY = 0.12  # segundos entre “pasos” de la serpiente (tick fijo)

# direcciones posibles (teclas) y su vector asociado en (x,y)
DIRS = {
    arcade.key.UP:    (0, 1),
    arcade.key.DOWN:  (0, -1),
    arcade.key.LEFT:  (-1, 0),
    arcade.key.RIGHT: (1, 0),
}

# definir la clase del juego, que hereda de arcade.Window
# * arcade.Window es a clase de Arcade que representa una ventana del juego
#   (maneja el bucle principal, eventos del teclado, redibujado, etc.).
# * Al heredar (class SnakeGame(arcade.Window):), tu clase “es una ventana” y
#   obtiene todos sus métodos/atributos, y tú puedes sobrescribir (“override”) los
#   callbacks que Arcade llama automáticamente:
# * __init__: crear la ventana y tu estado (con super().__init__(WIDTH,HEIGHT, "Título")).
# * on_draw: dibujar cada frame.
# * on_update(delta_time): actualizar la lógica del juego.
# * on_key_press(...): responder al teclado.
#
# En resumen: defines tu propio tipo de ventana de Arcade (tu juego) y personalizas su
# comportamiento implementando esos métodos. Luego, al instanciar SnakeGame() y
# llamar arcade.run(), Arcade ejecuta el bucle de eventos y va llamando on_update y
# on_draw por ti.

class SnakeGame(arcade.Window):
    print("Inicia el juego")

if __name__ == "__main__":
    print("Inicia el juego")