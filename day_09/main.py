import pandas as pd


from dataclasses import dataclass
from copy import deepcopy
from typing import List


@dataclass
class Motion:
    direction: str
    steps: int


@dataclass
class Position:
    x: int = 0
    y: int = 0


@dataclass
class Iteration:
    H: Position
    T: Position


class Simulation:
    def __init__(self):
        self.iterations: List[Iteration] = [Iteration(H=Position(), T=Position())]

    @property
    def current_H(self) -> Position:
        return self.iterations[-1].H

    @property
    def current_T(self) -> Position:
        return self.iterations[-1].T

    def execute_motion(self, motion: Motion) -> None:
        for step in range(motion.steps):
            new_iter = execute_step(self.current_H, self.current_T, motion.direction)
            self.iterations.append(new_iter)

    def execute_motions(self, motions: List[Motion]) -> None:
        for motion in motions:
            self.execute_motion(motion)

    @property
    def tail_positions(self) -> pd.DataFrame:
        df = pd.DataFrame([(i.T.x, i.T.y) for i in self.iterations])
        df.columns = ('x', 'y')
        return df


def execute_step(H: Position, T: Position, direction: str) -> Iteration:

    H = deepcopy(H)
    T = deepcopy(T)

    def go_up() -> None:
        if H.y > T.y:
            if H.x > T.x:
                T.x = H.x
                T.y += 1
            elif H.x < T.x:
                T.x = H.x
                T.y += 1
            else:
                T.y += 1
        elif H.y < T.y:
            if H.x > T.x:
                pass
            elif H.x < T.x:
                pass
            else:
                pass
        else:
            if H.x > T.x:
                pass
            elif H.x < T.x:
                pass
            else:
                pass
        H.y += 1

    def go_down() -> None:
        if H.y > T.y:
            if H.x > T.x:
                pass
            elif H.x < T.x:
                pass
            else:
                pass
        elif H.y < T.y:
            if H.x > T.x:
                T.x = H.x
                T.y -= 1
            elif H.x < T.x:
                T.x = H.x
                T.y -= 1
            else:
                T.y -= 1
        else:
            if H.x > T.x:
                pass
            elif H.x < T.x:
                pass
            else:
                pass
        H.y -= 1

    def go_left() -> None:
        if H.y > T.y:
            if H.x > T.x:
                pass
            elif H.x < T.x:
                T.x -= 1
                T.y = H.y
            else:
                pass
        elif H.y < T.y:
            if H.x > T.x:
                pass
            elif H.x < T.x:
                T.x -= 1
                T.y = H.y
            else:
                pass
        else:
            if H.x > T.x:
                pass
            elif H.x < T.x:
                T.x -= 1
            else:
                pass
        H.x -= 1

    def go_right() -> None:
        if H.y > T.y:
            if H.x > T.x:
                T.x += 1
                T.y = H.y
            if H.x < T.x:
                pass
            if H.x == T.x:
                pass
        if H.y < T.y:
            if H.x > T.x:
                T.x += 1
                T.y = H.y
            if H.x < T.x:
                pass
            if H.x == T.x:
                pass
        if H.y == T.y:
            if H.x > T.x:
                T.x += 1
            if H.x < T.x:
                pass
            if H.x == T.x:
                pass
        H.x += 1

    functions = {
        'U': go_up,
        'D': go_down,
        'L': go_left,
        'R': go_right
    }

    functions[direction]()

    return Iteration(H, T)


def read_input_row(row: str) -> Motion:
    direction, steps = row.split(' ')
    return Motion(direction, int(steps))


def main() -> None:
    with open('input.txt', 'r') as f:
        input_data = f.read().strip().split('\n')
    motions: List[Motion] = [read_input_row(row) for row in input_data]

    simulation = Simulation()
    simulation.execute_motions(motions)

    print(len(simulation.tail_positions.drop_duplicates()))


if __name__ == '__main__':
    main()
