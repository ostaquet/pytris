from abc import abstractmethod
import random
from multiprocessing.sharedctypes import synchronized

from common import Position, Cell, Command


class Tetromino:
    def __init__(self):
        self._pos: Position = Position(5, 1)
        self._angle: int = 0

    @abstractmethod
    def get_cell(self) -> Cell:
        pass

    @abstractmethod
    def get_positions(self) -> list[Position]:
        pass

    def apply_command(self, command: Command) -> None:
        if command == Command.DOWN:
            self._pos.y = self._pos.y + 1
        if command == Command.LEFT:
            self._pos.x = self._pos.x - 1
        if command == Command.RIGHT:
            self._pos.x = self._pos.x + 1
        if command == Command.TURN:
            self._angle = self._angle + 90
            if self._angle == 360:
                self._angle = 0

    def try_command(self, command: Command) -> list[Position]:
        # Save the current situation
        current_pos = self._pos
        current_angle = self._angle

        # Apply the command
        self.apply_command(command)

        # Remember future positions
        positions: list[Position] = self.get_positions()

        # Restore original situation
        self._pos = current_pos
        self._angle = current_angle

        # Return future positions
        return positions


class TetrominoI(Tetromino):
    def get_positions(self) -> list[Position]:
        if self._angle == 90 or self._angle == 180:
            return [Position(self._pos.x - 1, self._pos.y),
                    Position(self._pos.x, self._pos.y),
                    Position(self._pos.x + 1, self._pos.y),
                    Position(self._pos.x + 2, self._pos.y)]
        else:
            return [Position(self._pos.x, self._pos.y - 1),
                    Position(self._pos.x, self._pos.y),
                    Position(self._pos.x, self._pos.y + 1),
                    Position(self._pos.x, self._pos.y + 2)]

    def get_cell(self) -> Cell:
        return Cell.LIGHT_BLUE


class TetrominoO(Tetromino):
    def get_positions(self) -> list[Position]:
        return [Position(self._pos.x, self._pos.y),
                Position(self._pos.x + 1, self._pos.y),
                Position(self._pos.x, self._pos.y + 1),
                Position(self._pos.x + 1, self._pos.y + 1)]

    def get_cell(self) -> Cell:
        return Cell.YELLOW


class TetrominoT(Tetromino):
    def get_positions(self) -> list[Position]:
        if self._angle == 0:
            return [Position(self._pos.x, self._pos.y - 1),
                    Position(self._pos.x, self._pos.y),
                    Position(self._pos.x - 1, self._pos.y),
                    Position(self._pos.x + 1, self._pos.y)]
        if self._angle == 90:
            return [Position(self._pos.x, self._pos.y - 1),
                    Position(self._pos.x, self._pos.y),
                    Position(self._pos.x + 1, self._pos.y),
                    Position(self._pos.x, self._pos.y + 1)]
        if self._angle == 180:
            return [Position(self._pos.x - 1, self._pos.y),
                    Position(self._pos.x, self._pos.y),
                    Position(self._pos.x + 1, self._pos.y),
                    Position(self._pos.x, self._pos.y + 1)]
        if self._angle == 270:
            return [Position(self._pos.x, self._pos.y - 1),
                    Position(self._pos.x, self._pos.y),
                    Position(self._pos.x, self._pos.y + 1),
                    Position(self._pos.x - 1, self._pos.y)]

    def get_cell(self) -> Cell:
        return Cell.PURPLE


class TetrominoL(Tetromino):
    def get_positions(self) -> list[Position]:
        if self._angle == 0:
            return [Position(self._pos.x, self._pos.y + 1),
                    Position(self._pos.x, self._pos.y),
                    Position(self._pos.x + 1, self._pos.y),
                    Position(self._pos.x + 2, self._pos.y)]
        if self._angle == 90:
            return [Position(self._pos.x - 1, self._pos.y),
                    Position(self._pos.x, self._pos.y),
                    Position(self._pos.x, self._pos.y + 1),
                    Position(self._pos.x, self._pos.y + 2)]
        if self._angle == 180:
            return [Position(self._pos.x, self._pos.y - 1),
                    Position(self._pos.x, self._pos.y),
                    Position(self._pos.x - 1, self._pos.y),
                    Position(self._pos.x - 2, self._pos.y)]
        if self._angle == 270:
            return [Position(self._pos.x + 1, self._pos.y),
                    Position(self._pos.x, self._pos.y),
                    Position(self._pos.x, self._pos.y - 1),
                    Position(self._pos.x, self._pos.y - 2)]

    def get_cell(self) -> Cell:
        return Cell.ORANGE

class TetrominoJ(Tetromino):
    def get_positions(self) -> list[Position]:
        if self._angle == 0:
            return [Position(self._pos.x - 2, self._pos.y),
                    Position(self._pos.x - 1, self._pos.y),
                    Position(self._pos.x, self._pos.y),
                    Position(self._pos.x, self._pos.y + 1)]
        if self._angle == 90:
            return [Position(self._pos.x, self._pos.y - 2),
                    Position(self._pos.x, self._pos.y - 1),
                    Position(self._pos.x, self._pos.y),
                    Position(self._pos.x - 1, self._pos.y)]
        if self._angle == 180:
            return [Position(self._pos.x, self._pos.y - 1),
                    Position(self._pos.x, self._pos.y),
                    Position(self._pos.x + 1, self._pos.y),
                    Position(self._pos.x + 2, self._pos.y)]
        if self._angle == 270:
            return [Position(self._pos.x, self._pos.y),
                    Position(self._pos.x + 1, self._pos.y),
                    Position(self._pos.x, self._pos.y + 1),
                    Position(self._pos.x, self._pos.y + 2)]

    def get_cell(self) -> Cell:
        return Cell.DARK_BLUE


class TetrominoZ(Tetromino):
    def get_positions(self) -> list[Position]:
        if self._angle == 0 or self._angle == 180:
            return [Position(self._pos.x - 1, self._pos.y),
                    Position(self._pos.x, self._pos.y),
                    Position(self._pos.x, self._pos.y + 1),
                    Position(self._pos.x + 1, self._pos.y + 1)]
        else:
            return [Position(self._pos.x, self._pos.y - 1),
                    Position(self._pos.x, self._pos.y),
                    Position(self._pos.x - 1, self._pos.y),
                    Position(self._pos.x - 1, self._pos.y + 1)]

    def get_cell(self) -> Cell:
        return Cell.RED


class TetrominoS(Tetromino):
    def get_positions(self) -> list[Position]:
        if self._angle == 0 or self._angle == 180:
            return [Position(self._pos.x + 1, self._pos.y),
                    Position(self._pos.x, self._pos.y),
                    Position(self._pos.x, self._pos.y + 1),
                    Position(self._pos.x - 1, self._pos.y + 1)]
        else:
            return [Position(self._pos.x, self._pos.y - 1),
                    Position(self._pos.x, self._pos.y),
                    Position(self._pos.x + 1, self._pos.y),
                    Position(self._pos.x + 1, self._pos.y + 1)]

    def get_cell(self) -> Cell:
        return Cell.GREEN


def new_random_tetromino() -> Tetromino:
    random_int: int = random.randint(0, 6)
    if random_int == 0:
        return TetrominoO()
    if random_int == 1:
        return TetrominoI()
    if random_int == 2:
        return TetrominoT()
    if random_int == 3:
        return TetrominoL()
    if random_int == 4:
        return TetrominoJ()
    if random_int == 5:
        return TetrominoZ()
    if random_int == 6:
        return TetrominoS()
