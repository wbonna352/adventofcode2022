from __future__ import annotations
from .elements import Path, File


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


class ConsoleOutputInterpreter:
    def __init__(self, input_str: str):
        self.input_str = input_str

    @property
    def commands(self) -> list[Command]:
        return [Command(c) for c in self.input_str.split('$ ')][1:]
