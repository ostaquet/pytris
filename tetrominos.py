from enum import Enum
from typing import List
import random

from common import Cell, Position, Command


class TetriminoType(Enum):
    TETRIMINO_O = 0
    TETRIMINO_I = 1
    TETRIMINO_T = 2
    TETRIMINO_L = 3
    TETRIMINO_J = 4
    TETRIMINO_Z = 5
    TETRIMINO_S = 6

    def get_cell_type(self) -> Cell:
        if self == TetriminoType.TETRIMINO_O:
            return Cell.YELLOW
        elif self == TetriminoType.TETRIMINO_I:
            return Cell.LIGHT_BLUE
        elif self == TetriminoType.TETRIMINO_T:
            return Cell.PURPLE
        elif self == TetriminoType.TETRIMINO_L:
            return Cell.ORANGE
        elif self == TetriminoType.TETRIMINO_J:
            return Cell.DARK_BLUE
        elif self == TetriminoType.TETRIMINO_Z:
            return Cell.RED
        elif self == TetriminoType.TETRIMINO_S:
            return Cell.GREEN


def get_random() -> TetriminoType:
    random_int: int = random.randint(0, 6)
    if random_int == 0:
        return TetriminoType.TETRIMINO_O
    if random_int == 1:
        return TetriminoType.TETRIMINO_I
    if random_int == 2:
        return TetriminoType.TETRIMINO_T
    if random_int == 3:
        return TetriminoType.TETRIMINO_L
    if random_int == 4:
        return TetriminoType.TETRIMINO_J
    if random_int == 5:
        return TetriminoType.TETRIMINO_Z
    if random_int == 6:
        return TetriminoType.TETRIMINO_S


class Tetrinimo:

    def __init__(self):
        self._pos: Position = Position(5, 1)
        self._tetrinimo_type: TetriminoType = get_random()
        self._angle: int = 0

    def get_positions(self) -> List[Position]:
        if self._tetrinimo_type == TetriminoType.TETRIMINO_O:
            return [Position(self._pos.x, self._pos.y),
                    Position(self._pos.x + 1, self._pos.y),
                    Position(self._pos.x, self._pos.y + 1),
                    Position(self._pos.x + 1, self._pos.y + 1)]

        if self._tetrinimo_type == TetriminoType.TETRIMINO_I:
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

        if self._tetrinimo_type == TetriminoType.TETRIMINO_T:
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

        if self._tetrinimo_type == TetriminoType.TETRIMINO_L:
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

        if self._tetrinimo_type == TetriminoType.TETRIMINO_J:
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

        if self._tetrinimo_type == TetriminoType.TETRIMINO_Z:
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

        if self._tetrinimo_type == TetriminoType.TETRIMINO_S:
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

        if command == Command.TURN:
            if self._tetrinimo_type == TetriminoType.TETRIMINO_I:
                self._angle_add()
                self._angle_add()
                positions = self.get_positions()
                self._angle_sub()
                self._angle_sub()
            else:
                self._angle_add()
                positions = self.get_positions()
                self._angle_sub()

        return positions

    def _angle_add(self) -> None:
        self._angle = self._angle + 90
        if self._angle == 360:
            self._angle = 0

    def _angle_sub(self) -> None:
        self._angle = self._angle - 90
        if self._angle == -90:
            self._angle = 270

    def apply_command(self, command: Command) -> None:
        if command == Command.DOWN:
            self._pos.y = self._pos.y + 1
        if command == Command.LEFT:
            self._pos.x = self._pos.x - 1
        if command == Command.RIGHT:
            self._pos.x = self._pos.x + 1
        if command == Command.TURN:
            self._angle_add()
            if self._tetrinimo_type == TetriminoType.TETRIMINO_I:
                self._angle_add()

    def get_cell(self) -> Cell:
        return self._tetrinimo_type.get_cell_type()
