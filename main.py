from enum import Enum
from typing import List
import pygame


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Cell(Enum):
    EMPTY = 0
    RED = 1
    ORANGE = 2
    YELLOW = 3
    GREEN = 3
    LIGHT_BLUE = 4
    DARK_BLUE = 5
    PURPLE = 6


class Command(Enum):
    NONE = 0
    LEFT = 1
    RIGHT = 2
    DOWN = 3
    TURN = 4


class TetrinimoO:
    color: Cell = Cell.YELLOW

    def __init__(self):
        self.pos: Position = Position(5, 0)

    def get_positions(self) -> List[Position]:
        return [Position(self.pos.x, self.pos.y),
                Position(self.pos.x+1, self.pos.y),
                Position(self.pos.x, self.pos.y+1),
                Position(self.pos.x+1, self.pos.y+1)]

    def try_command(self, command: Command) -> list[Position]:
        positions: list[Position] = self.get_positions()

        if command == Command.DOWN:
            for pos in positions:
                pos.y = pos.y + 1

        if command == Command.LEFT:
            for pos in positions:
                pos.x = pos.x - 1

        if command == Command.RIGHT:
            for pos in positions:
                pos.x = pos.x + 1

        return positions

    def apply_command(self, command: Command) -> None:
        if command == Command.DOWN:
            self.pos.y = self.pos.y + 1
        if command == Command.LEFT:
            self.pos.x = self.pos.x - 1
        if command == Command.RIGHT:
            self.pos.x = self.pos.x + 1


# Set up colors
black = (0, 0, 0)
dark_grey = (43, 43, 43)
red = (255, 0, 36)
orange = (255, 144, 0)
yellow = (255, 224, 0)
green = (0, 186, 50)
light_blue = (0, 175, 231)
dark_blue = (0, 92, 162)
purple = (159, 30, 144)
white = (255, 255, 255)

# Set up square properties
square_size = 25


def is_position_valid(future_positions, board):
    for pos in future_positions:
        if pos.x < 0 or pos.x >= 12:
            return False
        if pos.y < 0 or pos.y >= 22:
            return False
        if board[pos.y][pos.x] != Cell.EMPTY:
            return False

    return True


def freeze(current_tetromino, board):
    for pos in current_tetromino.get_positions():
        board[pos.y][pos.x] = current_tetromino.color


def main():
    board = [[Cell.EMPTY for _ in range(12)] for _ in range(22)]

    # Initialize Pygame
    pygame.init()

    # Set up the game window
    window_width: int = 800
    window_height: int = 600
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Pytris")

    # Game variables
    running: bool = True

    current_tetromino = TetrinimoO()
    current_command: Command = Command.NONE
    count_cannot_go_down: int = 0
    last_tick: int = pygame.time.get_ticks()

    # Main game loop
    while running:
        # ****************** Handle events ******************
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_command = Command.LEFT
                if event.key == pygame.K_RIGHT:
                    current_command = Command.RIGHT
                if event.key == pygame.K_DOWN:
                    current_command = Command.DOWN
                if event.key == pygame.K_SPACE:
                    current_command = Command.TURN

        # ****************** Update game logic ******************
        # if is_collision(current_tetromino, board):
        #     # Game over
        #     running = False
        #
        future_positions: list[Position] = current_tetromino.try_command(current_command)
        if is_position_valid(future_positions, board):
            current_tetromino.apply_command(current_command)
        current_command = Command.NONE

        if pygame.time.get_ticks() - last_tick > 150:
            if count_cannot_go_down >= 2:
                freeze(current_tetromino, board)
                current_tetromino = TetrinimoO()

            future_positions: list[Position] = current_tetromino.try_command(Command.DOWN)

            if is_position_valid(future_positions, board):
                current_tetromino.apply_command(Command.DOWN)
                count_cannot_go_down = 0
            else:
                count_cannot_go_down = count_cannot_go_down + 1

            last_tick = pygame.time.get_ticks()

        # ****************** Draw the game ******************
        # Clear the screen
        window.fill(black)

        # Draw the board
        origin_x = (window_width - (12 * square_size)) / 2
        origin_y = (window_height - (22 * square_size)) / 2

        for x in range(12):
            for y in range(22):
                pygame.draw.rect(
                    window,
                    get_color_for(board[y][x]),
                    (origin_x + (x * square_size),
                     (origin_y + (y * square_size)),
                     square_size,
                     square_size))

        for pos in current_tetromino.get_positions():
            pygame.draw.rect(
                window,
                get_color_for(current_tetromino.color),
                (origin_x + (pos.x * square_size),
                 (origin_y + (pos.y * square_size)),
                 square_size,
                 square_size))

        # Update the display
        pygame.display.update()

    # Quit Pygame
    pygame.quit()


def get_color_for(cell: Cell) -> tuple[int, int, int]:
    if cell == Cell.EMPTY:
        return dark_grey
    elif cell == Cell.RED:
        return red
    elif cell == Cell.ORANGE:
        return orange
    elif cell == Cell.YELLOW:
        return yellow
    elif cell == Cell.GREEN:
        return green
    elif cell == Cell.LIGHT_BLUE:
        return light_blue
    elif cell == Cell.DARK_BLUE:
        return dark_blue
    elif cell == Cell.PURPLE:
        return purple
    else:
        return white


if __name__ == "__main__":
    main()
