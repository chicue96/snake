# snake_arcade.py
import random
import arcade

TILE = 20
COLS, ROWS = 32, 24
WIDTH, HEIGHT = COLS * TILE, ROWS * TILE
BG = arcade.color.DARK_SLATE_GRAY

MOVE_EVERY = 0.12  # segundos entre “pasos” de la serpiente (tick fijo)

DIRS = {
    arcade.key.UP:    (0, 1),
    arcade.key.DOWN:  (0, -1),
    arcade.key.LEFT:  (-1, 0),
    arcade.key.RIGHT: (1, 0),
}

class SnakeGame(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Snake - Arcade")
        arcade.set_background_color(BG)
        self.reset()

    def reset(self):
        self.snake = [(COLS // 2, ROWS // 2)]
        self.dir = (1, 0)
        self.to_grow = 0
        self.score = 0
        self.timer = 0.0
        self.food = self._spawn_food()

    def _spawn_food(self):
        while True:
            p = (random.randrange(COLS), random.randrange(ROWS))
            if p not in self.snake:
                return p

    def on_key_press(self, key, modifiers):
        if key in DIRS:
            nx, ny = DIRS[key]
            # Evitar reversa instantánea
            if (nx, ny) != (-self.dir[0], -self.dir[1]):
                self.dir = (nx, ny)
        elif key == arcade.key.R:
            self.reset()
        elif key == arcade.key.ESCAPE:
            arcade.close_window()

    def on_update(self, delta_time: float):
        # Acumulador para “tick” fijo (independiente del FPS)
        self.timer += delta_time
        while self.timer >= MOVE_EVERY:
            self.timer -= MOVE_EVERY
            self._step()

    def _step(self):
        hx, hy = self.snake[0]
        dx, dy = self.dir
        nx, ny = (hx + dx) % COLS, (hy + dy) % ROWS  # wrap en bordes
        # Colisión con cuerpo
        if (nx, ny) in self.snake:
            self.reset()
            return

        self.snake.insert(0, (nx, ny))  # mover cabeza

        if (nx, ny) == self.food:
            self.score += 1
            self.to_grow += 1
            self.food = self._spawn_food()

        if self.to_grow > 0:
            self.to_grow -= 1
        else:
            self.snake.pop()  # quitar cola

    def on_draw(self):
        arcade.start_render()
        # Dibujar serpiente
        for i, (x, y) in enumerate(self.snake):
            px, py = x * TILE, y * TILE
            size = TILE - 2
            arcade.draw_rectangle_filled(
                px + TILE / 2, py + TILE / 2, size, size,
                arcade.color.ELECTRIC_LIME if i == 0 else arcade.color.APPLE_GREEN
            )
        # Comida
        fx, fy = self.food
        arcade.draw_circle_filled(fx * TILE + TILE / 2, fy * TILE + TILE / 2, TILE / 3, arcade.color.RED_ORANGE)
        # UI
        arcade.draw_text(f"Score: {self.score}", 10, HEIGHT - 24, arcade.color.WHITE, 14)

if __name__ == "__main__":
    SnakeGame()
    arcade.run()
