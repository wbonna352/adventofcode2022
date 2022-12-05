import string


def find_halves_intersection(x: str) -> set:
    n = len(x)
    n_half = int(n / 2)
    half1 = set(x[:n_half])
    half2 = set(x[n_half:])
    return half1 & half2


def intersection_of_3_groups(x1: str, x2: str, x3: str) -> set:
    return set(x1) & set(x2) & set(x3)


def letter_to_value(x: str) -> int:
    values = {letter: value for value, letter in enumerate(string.ascii_letters, start=1)}
    return values.get(x)


def main() -> None:
    with open('input.txt', 'r') as f:
        input_data = f.read()

    input_data = input_data.strip().split('\n')

    def part_one() -> int:
        common_items = [find_halves_intersection(rucksack) for rucksack in input_data]
        common_items_priorities = [sum(letter_to_value(item) for item in items) for items in common_items]
        return sum(common_items_priorities)

    def part_two() -> int:
        groups = [input_data[i:i + 3] for i in range(0, len(input_data), 3)]
        common_items = [intersection_of_3_groups(*group) for group in groups]
        common_items_priorities = [sum(letter_to_value(item) for item in items) for items in common_items]
        return sum(common_items_priorities)

    print('Part one:', part_one())
    print('Part two:', part_two())


if __name__ == '__main__':
    main()
