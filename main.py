from typing import List

from common import *
from tetrominos import Tetrinimo

square_size: int = 25

def main():
    board: List[List[Cell]] = [[Cell.EMPTY for _ in range(12)] for _ in range(22)]

    pygame.init()

    window_width: int = 800
    window_height: int = 600
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Pytris")

    clock = pygame.time.Clock()
    pygame.time.set_timer(EVENT_GRAVITY, 150, 0)

    running: bool = True
    current_tetromino: Tetrinimo = Tetrinimo()
    current_command: Command = Command.NONE
    cannot_go_down: bool = False

    while running:
        # *******************************************************
        # ******************** Handle events ********************
        # *******************************************************
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
            if event.type == EVENT_GRAVITY:
                if cannot_go_down:
                    freeze(current_tetromino, board)
                    clean_board(board)
                    current_tetromino = Tetrinimo()
                    if not is_position_valid(current_tetromino.get_positions(), board):
                        running = False

                future_positions: list[Position] = current_tetromino.try_command(Command.DOWN)

                if is_position_valid(future_positions, board):
                    current_tetromino.apply_command(Command.DOWN)
                    cannot_go_down = False
                else:
                    cannot_go_down = True

        # *******************************************************
        # ****************** Update game logic ******************
        # *******************************************************
        future_positions: list[Position] = current_tetromino.try_command(current_command)
        if is_position_valid(future_positions, board) and not cannot_go_down:
            current_tetromino.apply_command(current_command)
        current_command = Command.NONE

        # *******************************************************
        # ******************** Draw the game ********************
        # *******************************************************
        window.fill(black)

        # Draw the board
        origin_x: int = int((window_width - (12 * square_size)) / 2)
        origin_y: int = int((window_height - (22 * square_size)) / 2)

        for x in range(12):
            for y in range(22):
                pygame.draw.rect(
                    window,
                    board[y][x].get_color(),
                    (origin_x + (x * square_size),
                     (origin_y + (y * square_size)),
                     square_size,
                     square_size))

        # Draw current tetromino
        for pos in current_tetromino.get_positions():
            pygame.draw.rect(
                window,
                current_tetromino.get_cell().get_color(),
                (origin_x + (pos.x * square_size),
                 (origin_y + (pos.y * square_size)),
                 square_size,
                 square_size))

        # Update the display
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(60)

    # Quit Pygame
    pygame.quit()


def is_position_valid(positions: List[Position], board: List[List[Cell]]) -> bool:
    for pos in positions:
        if pos.x < 0 or pos.x >= 12:
            return False
        if pos.y < 0 or pos.y >= 22:
            return False
        if board[pos.y][pos.x] != Cell.EMPTY:
            return False

    return True


def freeze(current_tetromino: Tetrinimo, board: List[List[Cell]]) -> None:
    for pos in current_tetromino.get_positions():
        board[pos.y][pos.x] = current_tetromino.get_cell()


def clean_board(board: List[List[Cell]]) -> None:
    row: int = 21
    while row >= 0:
        if is_row_complete(board[row]):
            shift(board, row)
        else:
            row = row - 1


def is_row_complete(row: List[Cell]) -> bool:
    for cell in row:
        if cell == Cell.EMPTY:
            return False
    return True


def shift(board: List[List[Cell]], row: int) -> None:
    for y in range(row, 0, -1):
        for x in range(12):
            board[y][x] = board[y-1][x]


if __name__ == "__main__":
    main()
