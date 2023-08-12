from enum import Enum
import pygame


class Cell(Enum):
    EMPTY = 0
    RED = 1
    ORANGE = 2
    YELLOW = 3
    GREEN = 3
    LIGHT_BLUE = 4
    DARK_BLUE = 5
    PURPLE = 6


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


def main():
    board = [[Cell.EMPTY for _ in range(12)] for _ in range(22)]

    # Initialize Pygame
    pygame.init()

    # Set up the game window
    window_width = 800
    window_height = 600
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Pytris")

    # Game variables
    running = True

    # Main game loop
    while running:
        # ****************** Handle events ******************
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # ****************** Update game logic ******************
        board[10][10] = Cell.PURPLE
        board[11][10] = Cell.PURPLE
        board[11][11] = Cell.PURPLE
        board[12][10] = Cell.PURPLE

        board[1][1] = Cell.LIGHT_BLUE
        board[2][1] = Cell.LIGHT_BLUE
        board[3][1] = Cell.LIGHT_BLUE
        board[4][1] = Cell.LIGHT_BLUE

        board[5][4] = Cell.YELLOW
        board[5][5] = Cell.YELLOW
        board[4][4] = Cell.YELLOW
        board[4][5] = Cell.YELLOW

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

        # Update the display
        pygame.display.update()

    # Quit Pygame
    pygame.quit()


def get_color_for(cell):
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