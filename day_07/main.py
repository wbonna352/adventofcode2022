from deviceLib.elements import Path, File
from deviceLib.console import Command, ConsoleOutputInterpreter
from deviceLib.device import Device


def main() -> None:
    with open('input.txt', 'r') as f:
        input_data = f.read()

    device = Device()
    device.map_from_console_output(input_data)

    def part_one() -> int:
        def calc(path):
            limit = 100000
            counted_paths = sum([p.size for p in path.elements.values() if isinstance(p, Path) and p.size <= limit])
            return counted_paths + sum([calc(p) for p in path.elements.values() if isinstance(p, Path)])

        return calc(device.main_path)

    def part_two() -> int:
        available_space = 70000000
        space_needed = 30000000
        max_usage = available_space - space_needed
        current_usage = sum([e.size for e in device.main_path.elements.values()])
        space_to_be_free_up = current_usage - max_usage

        def calc(path):
            curr_layer = [p for p in path.elements.values() if
                          isinstance(p, Path) and p.size >= space_to_be_free_up]
            values = [p.size for p in curr_layer]
            return [values, [calc(p) for p in curr_layer]]

        nested = calc(device.main_path)

        def flatten(x: list) -> list:
            if not (bool(x)):
                return x
            if isinstance(x[0], list):
                return flatten(*x[:1]) + flatten(x[1:])
            return x[:1] + flatten(x[1:])

        return min(flatten(nested))

    print('Part one:', part_one())
    print('Part two:', part_two())


if __name__ == '__main__':
    main()
