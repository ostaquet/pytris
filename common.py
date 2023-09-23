from enum import Enum
import pygame

# Défini un événement custom
EVENT_GRAVITE = pygame.USEREVENT + 1


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Cell(Enum):
    EMPTY = 0
    RED = 1
    ORANGE = 2
    YELLOW = 3
    GREEN = 4
    LIGHT_BLUE = 5
    DARK_BLUE = 6
    PURPLE = 7

    def get_color(self) -> tuple[int, int, int]:
        if self == Cell.EMPTY:
            return dark_grey
        elif self == Cell.RED:
            return red
        elif self == Cell.ORANGE:
            return orange
        elif self == Cell.YELLOW:
            return yellow
        elif self == Cell.GREEN:
            return green
        elif self == Cell.LIGHT_BLUE:
            return light_blue
        elif self == Cell.DARK_BLUE:
            return dark_blue
        elif self == Cell.PURPLE:
            return purple
        else:
            return white


class Command(Enum):
    NONE = 0
    LEFT = 1
    RIGHT = 2
    DOWN = 3
    TURN = 4


# Set up colors
black: tuple[int, int, int] = (0, 0, 0)
dark_grey: tuple[int, int, int] = (43, 43, 43)
red: tuple[int, int, int] = (255, 0, 36)
orange: tuple[int, int, int] = (255, 144, 0)
yellow: tuple[int, int, int] = (255, 224, 0)
green: tuple[int, int, int] = (0, 186, 50)
light_blue: tuple[int, int, int] = (0, 175, 231)
dark_blue: tuple[int, int, int] = (0, 92, 162)
purple: tuple[int, int, int] = (159, 30, 144)
white: tuple[int, int, int] = (255, 255, 255)
