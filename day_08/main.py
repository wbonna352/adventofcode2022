import numpy as np


def digit_array_from_str(x: str) -> np.array:
    matrix = [[e for e in line] for line in x.strip().split('\n')]
    return np.array(matrix, dtype=int)


def tree_visible(r: int, c: int, array: np.array) -> bool:
    v = array[r, c]
    left = not np.any(array[r, :c] >= v)
    right = not np.any(array[r, (c+1):] >= v)
    top = not np.any(array[:r, c] >= v)
    bottom = not np.any(array[(r+1):, c] >= v)
    return np.any([left, right, top, bottom])


def main() -> None:
    with open('input.txt') as f:
        input_data = f.read()
    trees = digit_array_from_str(input_data)

    value = 0
    for r in range(trees.shape[0]):
        for c in range(trees.shape[1]):
            value += int(tree_visible(r, c, trees))

    print(value)


if __name__ == '__main__':
    main()
