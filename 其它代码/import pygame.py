import pygame
import random

# Constants
WIDTH, HEIGHT = 300, 600
GRID_SIZE = 30
FPS = 30

# Tetris shapes
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]]
]

SHAPES_COLORS = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (255, 255, 0),  # Yellow
    (255, 165, 0),  # Orange
    (128, 0, 128),  # Purple
    (0, 255, 255)   # Cyan
]

class Tetris:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()

        self.grid = [[0] * (WIDTH // GRID_SIZE) for _ in range(HEIGHT // GRID_SIZE)]

        self.current_shape = self.new_shape()
        self.current_color = self.new_color()
        self.current_row = 0
        self.current_col = WIDTH // (2 * GRID_SIZE) - len(self.current_shape[0]) // 2

        self.score = 0

    def new_shape(self):
        return random.choice(SHAPES)

    def new_color(self):
        return random.choice(SHAPES_COLORS)

    def draw_grid(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] > 0:
                    pygame.draw.rect(self.screen, SHAPES_COLORS[self.grid[row][col] - 1],
                                     (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    def draw_shape(self):
        for row in range(len(self.current_shape)):
            for col in range(len(self.current_shape[row])):
                if self.current_shape[row][col] == 1:
                    pygame.draw.rect(self.screen, self.current_color,
                                     ((self.current_col + col) * GRID_SIZE, (self.current_row + row) * GRID_SIZE,
                                      GRID_SIZE, GRID_SIZE))

    def check_collision(self):
        for row in range(len(self.current_shape)):
            for col in range(len(self.current_shape[row])):
                if (
                    self.current_row + row >= len(self.grid) or
                    self.current_col + col >= len(self.grid[0]) or
                    self.current_col + col < 0 or
                    self.grid[self.current_row + row][self.current_col + col] > 0
                ):
                    return True
        return False

    def merge_shape(self):
        for row in range(len(self.current_shape)):
            for col in range(len(self.current_shape[row])):
                if self.current_shape[row][col] == 1:
                    self.grid[self.current_row + row][self.current_col + col] = self.current_color

    def check_line_clear(self):
        lines_to_clear = [row for row in range(len(self.grid)) if all(self.grid[row])]

        for row in lines_to_clear:
            del self.grid[row]
            self.grid.insert(0, [0] * (WIDTH // GRID_SIZE))

        self.score += len(lines_to_clear)

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.current_col -= 1
                        if self.check_collision():
                            self.current_col += 1
                    elif event.key == pygame.K_RIGHT:
                        self.current_col += 1
                        if self.check_collision():
                            self.current_col -= 1
                    elif event.key == pygame.K_DOWN:
                        self.current_row += 1
                        if self.check_collision():
                            self.current_row -= 1
                    elif event.key == pygame.K_UP:
                        self.rotate_shape()

            self.current_row += 1
            if self.check_collision():
                self.current_row -= 1
                self.merge_shape()
                self.check_line_clear()
                self.current_shape = self.new_shape()
                self.current_color = self.new_color()
                self.current_row = 0
                self.current_col = WIDTH // (2 * GRID_SIZE) - len(self.current_shape[0]) // 2

            self.screen.fill((0, 0, 0))
            self.draw_grid()
            self.draw_shape()
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

    def rotate_shape(self):
        self.current_shape = list(zip(*reversed(self.current_shape)))

if __name__ == "__main__":
    Tetris().run()
