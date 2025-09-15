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

DIRS = {
    arcade.key.UP:    (0, 1), # (x,y)
    arcade.key.DOWN:  (0, -1),
    arcade.key.LEFT:  (-1, 0),
    arcade.key.RIGHT: (1, 0),
}

if __name__ == "__main__":
    print("Inicia el juego")