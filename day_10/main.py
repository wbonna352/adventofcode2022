from enum import Enum, auto
from dataclasses import dataclass
from typing import List


class InstructionType(Enum):
    NOOP = auto()
    ADDX = auto()


@dataclass(frozen=True)
class Cycle:
    number: int
    X: int
    V: int
    final_number: int

    @property
    def signal_strength(self) -> int:
        return self.number * self.X


class Instruction:
    def __init__(self, text: str):
        self.text = text

    @property
    def type(self) -> InstructionType:
        if self.text.startswith("noop"):
            return InstructionType.NOOP
        elif self.text.startswith("addx"):
            return InstructionType.ADDX
        else:
            raise ValueError(f"Unknown instruction: {self.text}")

    @property
    def duration(self) -> int:
        if self.type == InstructionType.NOOP:
            return 1
        if self.type == InstructionType.ADDX:
            return 2

    @property
    def value(self) -> int:
        if self.type == InstructionType.NOOP:
            return 0
        return int(self.text.split(" ")[1])


class ClockCircuit:
    def __init__(self, X: int = 1):
        self.X = X
        self.cycles: List[Cycle] = [Cycle(1, self.X, 0, 1)]

    @property
    def last_cycle(self) -> Cycle:
        return self.cycles[-1]

    def execute_instruction(self, instruction: Instruction):
        cycle = Cycle(
            number=self.last_cycle.final_number,
            X=self.last_cycle.X+self.last_cycle.V,
            V=instruction.value,
            final_number=self.last_cycle.final_number + instruction.duration
        )
        self.cycles.append(cycle)

    def execute_instructions(self, instructions: List[Instruction]):
        for instruction in instructions:
            self.execute_instruction(instruction)

    def cycle_signal_value(self, number) -> int:
        X = self.X
        for cycle in self.cycles:
            if cycle.number > number:
                break
            X = cycle.X
        return number*X


def main() -> None:
    with open('input.txt') as f:
        input_data = f.read().strip().split('\n')
    instructions: List[Instruction] = [Instruction(line) for line in input_data]

    clock_circuit = ClockCircuit()
    clock_circuit.execute_instructions(instructions)

    part_one = sum(clock_circuit.cycle_signal_value(i) for i in [20, 60, 100, 140, 180, 220])
    print(part_one)


if __name__ == '__main__':
    main()
