from __future__ import annotations
from .elements import Path
from .console import ConsoleOutputInterpreter


class Device:
    def __init__(self):
        self.main_path = Path('/', None)
        self.cwd = self.main_path

    def map_from_console_output(self, output_str: str):
        coi = ConsoleOutputInterpreter(output_str)
        for c in coi.commands:
            c.execute(self)
