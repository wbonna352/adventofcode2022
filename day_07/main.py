class File:
    def __init__(self, name: str, size: int, **kwargs):
        self.name = name
        self.size = int(size)
        self.path = kwargs.get('path')

    @property
    def full_name(self) -> str:
        if self.path:
            return f'{self.path.full_name}/{self.name}'
        return self.name


class ConsoleOutputInterpreter:
    def __init__(self, input_str: str):
        self.input_str = input_str

    @property
    def commands(self):
        return [Command(c) for c in self.input_str.split('$ ')][1:]


class Device:
    def __init__(self):
        self.main_path = Path('/')
        self.cwd = self.main_path
        self.e = []

    def map_from_console_output(self, output_str: str):
        coi = ConsoleOutputInterpreter(output_str)
        for c in coi.commands:
            c.execute(self)


class Path:
    def __init__(self, name: str, **kwargs):
        self.name = name
        self.elements = dict()
        self.path = kwargs.get('path')

    @property
    def full_name(self) -> str:
        if self.path:
            return f'{self.path.full_name}/{self.name}'
        return self.name

    @property
    def size(self):
        def flatten(path):
            return sum([f.size for f in path.elements.values() if isinstance(f, File)]) + sum(
                [flatten(p) for p in path.elements.values() if isinstance(p, Path)])

        return flatten(self)


class Command:
    def __init__(self, command: str):
        self._command = command
        self._command_output_split()

    def _command_output_split(self) -> None:
        self.command, *self.output = self._command.split('\n')
        if self.output == ['']:
            self.output = None
        if self.output:
            self.output = [el for el in self.output if el != '']

    def execute(self, d: Device) -> None:

        def ls():
            for e in self.output:
                size, name = e.split(' ', maxsplit=1)
                if size == 'dir':
                    d.cwd.elements[name] = Path(name, path=d.cwd)
                else:
                    d.cwd.elements[name] = File(name, size, path=d.cwd)

        def cd_to_start():
            d.cwd = d.main_path

        def cd_out():
            d.cwd = d.cwd.path

        def cd_in(name: str):
            d.cwd = d.cwd.elements.get(name)

        if self.command == 'ls':
            ls()
        elif self.command == 'cd /':
            cd_to_start()
        elif self.command == 'cd ..':
            cd_out()
        elif self.command[:2] == 'cd':
            cd_in(self.command[3:])


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
