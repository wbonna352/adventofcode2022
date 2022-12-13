import unittest
from parameterized import parameterized
from main import Position, Moves


class TestTailMove(unittest.TestCase):

    @parameterized.expand([
        [Position(0, 0), Position(0, 0), Position(0, 0)],
        [Position(0, 0), Position(1, 1), Position(1, 1)],
        [Position(0, 0), Position(2, 2), Position(1, 1)],
        [Position(0, 0), Position(-2, 2), Position(-1, 1)],
        [Position(0, 0), Position(2, -2), Position(1, -1)],
        [Position(0, 0), Position(-2, -2), Position(-1, -1)],
        [Position(0, 0), Position(2, 0), Position(1, 0)],
        [Position(0, 0), Position(-2, 0), Position(-1, 0)],
        [Position(0, 0), Position(0, 2), Position(0, 1)],
        [Position(0, 0), Position(0, -2), Position(0, -1)]
    ])
    def test_tail_move(self, H: Position, T: Position, expected: Position) -> None:
        Moves.tail_move(H, T)
        self.assertEqual(expected, T)


if __name__ == '__main__':
    unittest.main()
