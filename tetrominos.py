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
        self.pos: Position = Position(5, 0)
        self.tetrinimo_type: TetriminoType = get_random()
        self.angle: int = 0

    def get_positions(self) -> List[Position]:
        if self.tetrinimo_type == TetriminoType.TETRIMINO_O:
            return [Position(self.pos.x, self.pos.y),
                    Position(self.pos.x+1, self.pos.y),
                    Position(self.pos.x, self.pos.y+1),
                    Position(self.pos.x+1, self.pos.y+1)]

        if self.tetrinimo_type == TetriminoType.TETRIMINO_I:
            if self.angle == 90 or self.angle == 180:
                return [Position(self.pos.x - 1, self.pos.y),
                        Position(self.pos.x, self.pos.y),
                        Position(self.pos.x + 1, self.pos.y),
                        Position(self.pos.x + 2, self.pos.y)]
            else:
                return [Position(self.pos.x, self.pos.y - 1),
                        Position(self.pos.x, self.pos.y),
                        Position(self.pos.x, self.pos.y + 1),
                        Position(self.pos.x, self.pos.y + 2)]

        if self.tetrinimo_type == TetriminoType.TETRIMINO_T:
            if self.angle == 0:
                return [Position(self.pos.x, self.pos.y-1),
                        Position(self.pos.x, self.pos.y),
                        Position(self.pos.x - 1, self.pos.y),
                        Position(self.pos.x + 1, self.pos.y)]
            if self.angle == 90:
                return [Position(self.pos.x, self.pos.y - 1),
                        Position(self.pos.x, self.pos.y),
                        Position(self.pos.x + 1, self.pos.y),
                        Position(self.pos.x, self.pos.y + 1)]
            if self.angle == 180:
                return [Position(self.pos.x - 1, self.pos.y),
                        Position(self.pos.x, self.pos.y),
                        Position(self.pos.x + 1, self.pos.y),
                        Position(self.pos.x, self.pos.y + 1)]
            if self.angle == 270:
                return [Position(self.pos.x, self.pos.y-1),
                        Position(self.pos.x, self.pos.y),
                        Position(self.pos.x, self.pos.y+1),
                        Position(self.pos.x-1, self.pos.y)]

        if self.tetrinimo_type == TetriminoType.TETRIMINO_L:
            if self.angle == 0:
                return [Position(self.pos.x, self.pos.y + 1),
                        Position(self.pos.x, self.pos.y),
                        Position(self.pos.x + 1, self.pos.y),
                        Position(self.pos.x + 2, self.pos.y)]
            if self.angle == 90:
                return [Position(self.pos.x-1, self.pos.y),
                        Position(self.pos.x, self.pos.y),
                        Position(self.pos.x, self.pos.y + 1),
                        Position(self.pos.x, self.pos.y + 2)]
            if self.angle == 180:
                return [Position(self.pos.x, self.pos.y-1),
                        Position(self.pos.x, self.pos.y),
                        Position(self.pos.x - 1, self.pos.y),
                        Position(self.pos.x - 2, self.pos.y)]
            if self.angle == 270:
                return [Position(self.pos.x+1, self.pos.y),
                        Position(self.pos.x, self.pos.y),
                        Position(self.pos.x, self.pos.y - 1),
                        Position(self.pos.x, self.pos.y - 2)]

        if self.tetrinimo_type == TetriminoType.TETRIMINO_J:
            if self.angle == 0:
                return [Position(self.pos.x-2, self.pos.y),
                        Position(self.pos.x-1, self.pos.y),
                        Position(self.pos.x, self.pos.y),
                        Position(self.pos.x, self.pos.y+1)]
            if self.angle == 90:
                return [Position(self.pos.x, self.pos.y-2),
                        Position(self.pos.x, self.pos.y-1),
                        Position(self.pos.x, self.pos.y),
                        Position(self.pos.x-1, self.pos.y)]
            if self.angle == 180:
                return [Position(self.pos.x, self.pos.y-1),
                        Position(self.pos.x, self.pos.y),
                        Position(self.pos.x + 1, self.pos.y),
                        Position(self.pos.x + 2, self.pos.y)]
            if self.angle == 270:
                return [Position(self.pos.x, self.pos.y),
                        Position(self.pos.x+1, self.pos.y),
                        Position(self.pos.x, self.pos.y + 1),
                        Position(self.pos.x, self.pos.y + 2)]

        if self.tetrinimo_type == TetriminoType.TETRIMINO_Z:
            if self.angle == 0 or self.angle == 180:
                return [Position(self.pos.x-1, self.pos.y),
                        Position(self.pos.x, self.pos.y),
                        Position(self.pos.x, self.pos.y+1),
                        Position(self.pos.x+1, self.pos.y+1)]
            else:
                return [Position(self.pos.x, self.pos.y-1),
                        Position(self.pos.x, self.pos.y),
                        Position(self.pos.x-1, self.pos.y),
                        Position(self.pos.x-1, self.pos.y+1)]

        if self.tetrinimo_type == TetriminoType.TETRIMINO_S:
            if self.angle == 0 or self.angle == 180:
                return [Position(self.pos.x+1, self.pos.y),
                        Position(self.pos.x, self.pos.y),
                        Position(self.pos.x, self.pos.y+1),
                        Position(self.pos.x-1, self.pos.y+1)]
            else:
                return [Position(self.pos.x, self.pos.y-1),
                        Position(self.pos.x, self.pos.y),
                        Position(self.pos.x+1, self.pos.y),
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

        if command == Command.TURN:
            if self.tetrinimo_type == TetriminoType.TETRIMINO_I:
                self.angle_add()
                self.angle_add()
                positions = self.get_positions()
                self.angle_sub()
                self.angle_sub()
            else:
                self.angle_add()
                positions = self.get_positions()
                self.angle_sub()

        return positions

    def angle_add(self):
        self.angle = self.angle + 90
        if self.angle == 360:
            self.angle = 0

    def angle_sub(self):
        self.angle = self.angle - 90
        if self.angle == -90:
            self.angle = 270

    def apply_command(self, command: Command) -> None:
        if command == Command.DOWN:
            self.pos.y = self.pos.y + 1
        if command == Command.LEFT:
            self.pos.x = self.pos.x - 1
        if command == Command.RIGHT:
            self.pos.x = self.pos.x + 1
        if command == Command.TURN:
            self.angle_add()
            if self.tetrinimo_type == TetriminoType.TETRIMINO_I:
                self.angle_add()

    def get_cell(self) -> Cell:
        return self.tetrinimo_type.get_cell_type()