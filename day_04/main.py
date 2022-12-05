class Pair:
    def __init__(self, input_str: str):
        self._input_str = input_str
        self._create_elves()

    def _create_elves(self) -> None:
        elves_inputs = self._input_str.split(',')
        self.elf1 = self.Elf(elves_inputs[0])
        self.elf2 = self.Elf(elves_inputs[1])

    class Elf:
        def __init__(self, input_str: str):
            self._input_str = input_str

        @property
        def set(self) -> set:
            start, end = self._input_str.split('-')
            return set(range(int(start), int(end) + 1))

    @property
    def is_subset(self) -> bool:
        set1 = self.elf1.set
        set2 = self.elf2.set
        return set1.issubset(set2) or set2.issubset(set1)

    @property
    def is_overlap(self) -> bool:
        return bool(self.elf1.set & self.elf2.set)


def main() -> None:
    with open('input.txt') as f:
        input_data = f.read()
    input_data = input_data.strip().split('\n')

    pairs = [Pair(i) for i in input_data]

    # part one
    is_subsets = [pair.is_subset for pair in pairs]
    print('Part one:', sum(is_subsets))

    # part two
    is_overlap = [pair.is_overlap for pair in pairs]
    print('Part two:', sum(is_overlap))


if __name__ == '__main__':
    main()
