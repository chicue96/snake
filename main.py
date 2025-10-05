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
    def __init__(self):
        # Constructor de tu clase ventana/juego. Se ejecuta al crear SnakeGame().
        super().__init__(WIDTH, HEIGHT, "Snake - Arcade")  # Llama al __init__ de arcade.Window: crea la ventana con tamaño y título.
        arcade.set_background_color(BG)                    # Fija el color de fondo que usará clear() en cada frame.
        self.reset()                                       # Resetea/Inicializa el estado del juego (serpiente, dirección, comida, puntaje).

    def reset(self):
        # self es la referencia a la instancia actual sobre la que se está ejecutando un método.
        """Reinicia el estado del juego (serpiente, dirección, puntaje, temporizador y comida)."""
        # Serpiente: lista de celdas (x, y) en el grid. Empieza en el centro del tablero.
        # COLS // 2 y ROWS // 2 son divisiones enteras para obtener la celda central.
        self.snake = [(COLS // 2, ROWS // 2)]
        # Dirección inicial (dx, dy). (1, 0) = hacia la derecha.
        self.dir = (1, 0)
        # Segmentos pendientes por crecer después de comer. Cada “tick” consume 1 hasta volver a 0.
        self.to_grow = 0
        # Puntaje inicial.
        self.score = 0
        # Acumulador de tiempo para mover por “ticks” fijos (independiente del FPS).
        self.timer = 0.0
        # Genera una posición de comida aleatoria que no choque con el cuerpo de la serpiente.
        self.food = self._spawn_food()

    def _spawn_food(self):
        """Elige y devuelve una celda libre del tablero para colocar la comida."""
        while True:
            # Genera una posición aleatoria dentro de los límites del grid.
            # random.randrange(N) produce un entero en el rango [0, N)
            p = (random.randrange(COLS), random.randrange(ROWS))
            # Asegura que la comida no aparezca sobre el cuerpo de la serpiente
            if p not in self.snake:
                return p  # Devuelve la tupla (x, y) y termina la función
    
    def on_key_press(self, key, modifiers):
        # Callback de Arcade: se llama cuando el usuario PRESIONA una tecla.
        # 'key' es el código de la tecla; 'modifiers' indica si había Shift/Ctrl/Alt (no lo usamos aquí).
        if key in DIRS:
            # Si la tecla es una direccional válida (arriba/abajo/izquierda/derecha) registrada en DIRS...
            nx, ny = DIRS[key]  # Obtenemos el vector de movimiento deseado para esa tecla.
            # Evitar reversa instantánea: no permitir girar 180° sobre sí mismo (p. ej., de derecha a izquierda).
            if (nx, ny) != (-self.dir[0], -self.dir[1]):
                self.dir = (nx, ny)  # Actualizamos la dirección actual de la serpiente.
        elif key == arcade.key.R:
            self.reset()  # 'R' reinicia el juego (estado inicial: serpiente, puntaje, comida, etc.).
        elif key == arcade.key.ESCAPE:
            arcade.close_window()  # 'Esc' cierra la ventana y finaliza la aplicación.

if __name__ == "__main__":
    print("Inicia el juego")