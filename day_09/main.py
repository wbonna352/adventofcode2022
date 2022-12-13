from enum import Enum
import numpy as np
import pandas as pd
from dataclasses import dataclass
from copy import deepcopy
from typing import List, Union


class Direction(Enum):
    UP = 'U'
    DOWN = 'D'
    LEFT = 'L'
    RIGHT = 'R'


@dataclass
class Motion:
    direction: Union[Direction, str]
    steps: int

    def __post_init__(self):
        if isinstance(self.direction, str):
            self.direction = Direction(self.direction)


@dataclass
class Position:
    x: int = 0
    y: int = 0


class Iteration:
    def __init__(self, knots_number: int):
        self.knots_number = knots_number
        self.knots: List[Position] = [Position() for _ in range(knots_number)]

    @property
    def H(self) -> Position:
        return self.knots[0]

    @property
    def T(self) -> Position:
        return self.knots[-1]


class Simulation:
    def __init__(self, knots_number: int):
        self.knots_number = knots_number
        self.iterations: List[Iteration] = [Iteration(knots_number)]

    @property
    def last_iteration(self) -> Iteration:
        return self.iterations[-1]

    def execute_motion(self, motion: Motion) -> None:
        for step in range(motion.steps):
            new_iter = deepcopy(self.last_iteration)
            Moves.head_move(new_iter.knots[0], motion.direction)
            for i in range(1, self.knots_number):
                Moves.tail_move(new_iter.knots[i - 1], new_iter.knots[i])
            self.iterations.append(new_iter)

    def execute_motions(self, motions: List[Motion]) -> None:
        for motion in motions:
            self.execute_motion(motion)

    @property
    def tail_positions(self) -> pd.DataFrame:
        df = pd.DataFrame([(i.T.x, i.T.y) for i in self.iterations])
        df.columns = ('x', 'y')
        return df


class Moves:

    @staticmethod
    def head_move(H: Position, direction: Direction) -> None:
        if direction == Direction.UP:
            H.y += 1
        elif direction == Direction.DOWN:
            H.y -= 1
        elif direction == Direction.LEFT:
            H.x -= 1
        elif direction == Direction.RIGHT:
            H.x += 1

    @staticmethod
    def tail_move(H: Position, T: Position) -> None:
        x_diff = T.x - H.x
        y_diff = T.y - H.y

        if x_diff > 1:
            if y_diff > 1:
                T.x = H.x + 1
                T.y = H.y + 1
            elif y_diff < -1:
                T.x = H.x + 1
                T.y = H.y - 1
            else:
                T.x = H.x + 1
                T.y = H.y
        elif x_diff < -1:
            if y_diff > 1:
                T.x = H.x - 1
                T.y = H.y + 1
            elif y_diff < -1:
                T.x = H.x - 1
                T.y = H.y - 1
            else:
                T.x = H.x - 1
                T.y = H.y
        else:
            if y_diff > 1:
                T.x = H.x
                T.y = H.y + 1
            elif y_diff < -1:
                T.x = H.x
                T.y = H.y - 1
            else:
                pass


def read_input_row(row: str) -> Motion:
    direction, steps = row.split(' ')
    return Motion(direction, int(steps))


def main() -> None:
    with open('input.txt', 'r') as f:
        input_data = f.read().strip().split('\n')
    motions: List[Motion] = [read_input_row(row) for row in input_data]

    def part_one() -> int:
        simulation = Simulation(knots_number=2)
        simulation.execute_motions(motions)
        return len(simulation.tail_positions.drop_duplicates())

    def part_two() -> int:
        simulation = Simulation(knots_number=10)
        simulation.execute_motions(motions)
        return len(simulation.tail_positions.drop_duplicates())

    print(f'Part one: {part_one()}')
    print(f'Part two: {part_two()}')


if __name__ == '__main__':
    main()
