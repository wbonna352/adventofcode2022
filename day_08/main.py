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


def scenic_score(r: int, c: int, array: np.array) -> int:
    v = array[r, c]

    def count_trees(value: int, vector: np.array) -> int:
        trees = 0
        for i in vector:
            trees += 1
            if i >= value:
                break
        return trees

    vectors = {
        'left': array[r, :c][::-1],
        'right': array[r, (c+1):],
        'top': array[:r, c][::-1],
        'bottom': array[(r+1):, c]
    }

    return np.prod([count_trees(v, vector) for vector in vectors.values()])


def main() -> None:
    with open('input.txt') as f:
        input_data = f.read()
    trees = digit_array_from_str(input_data)

    visible_count = 0
    max_scenic_score = 0
    for r in range(trees.shape[0]):
        for c in range(trees.shape[1]):
            visible_count += int(tree_visible(r, c, trees))
            if (tree_scenic_score := scenic_score(r, c, trees)) > max_scenic_score:
                max_scenic_score = tree_scenic_score

    print('Part one: ', visible_count)
    print('Part two: ', max_scenic_score)


if __name__ == '__main__':
    main()
