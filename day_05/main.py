import re


class Stacks:
    def __init__(self, starting_stacks: str):
        self._starting_stacks = starting_stacks
        self._read_starting_stacks()
        self.stacks = self.starting_stacks.copy()

    def _read_starting_stacks(self):
        stacks_layers = [row[1::4] for row in self._starting_stacks.split('\n')]
        self.stacks_names = stacks_layers.pop()
        self.starting_stacks = {name: list() for name in self.stacks_names}
        for i, name in enumerate(self.stacks_names):
            for layer in stacks_layers[::-1]:
                try:
                    crate = layer[i]
                except IndexError:
                    continue
                if crate != ' ':
                    self.starting_stacks[name].append(crate)

    def execute_procedure9000(self, procedure: str) -> None:
        pattern = r'move (\d+) from (\d+) to (\d+)'
        result = re.search(pattern, procedure)
        n, stacks_from, stacks_to = result.groups()
        for move in range(int(n)):
            self.stacks[stacks_to].append(self.stacks[stacks_from].pop())

    def execute_procedure9001(self, procedure: str) -> None:
        pattern = r'move (\d+) from (\d+) to (\d+)'
        result = re.search(pattern, procedure)
        n, stacks_from, stacks_to = result.groups()
        n = int(n)
        crates = self.stacks[stacks_from][-n:]
        del self.stacks[stacks_from][-n:]
        self.stacks[stacks_to].extend(crates)

    def print_output(self) -> None:
        print(''.join([self.stacks[stack][-1] for stack in self.stacks_names]))


def main() -> None:
    with open('input.txt') as f:
        input_data = f.read()

    starting_stacks, procedures = input_data.split('\n\n')

    procedures = [p for p in procedures.strip().split('\n')]
    stacks9000 = Stacks(starting_stacks)
    stacks9001 = Stacks(starting_stacks)

    for procedure in procedures:
        stacks9000.execute_procedure9000(procedure)
        stacks9001.execute_procedure9001(procedure)

    stacks9000.print_output()
    stacks9001.print_output()


if __name__ == '__main__':
    main()
