from __future__ import annotations


class Path:
    def __init__(self, name: str, path: Path | None):
        self.name = name
        self.elements = dict()
        self.path = path

    @property
    def full_name(self) -> str:
        if self.path:
            return f'{self.path.full_name}/{self.name}'
        return self.name

    @property
    def size(self) -> int:
        def flatten(path: Path) -> int:
            return sum([f.size for f in path.elements.values() if isinstance(f, File)]) + sum(
        [flatten(p) for p in path.elements.values() if isinstance(p, Path)])

        return flatten(self)


class File:
    def __init__(self, name: str, size: int, path: Path):
        self.name = name
        self.size = int(size)
        self.path = path

    @property
    def full_name(self) -> str:
        if self.path:
            return f'{self.path.full_name}/{self.name}'
        return self.name
