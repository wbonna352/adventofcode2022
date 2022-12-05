def is_subset(start1: int, end1: int, start2: int, end2: int) -> bool:
    if (start1 <= start2 and end1 >= end2) or (start1 >= start2 and end1 <= end2):
        return True
    return False


def is_overlap(start1: int, end1: int, start2: int, end2: int) -> bool:
    elf1 = set(range(start1, end1+1))
    elf2 = set(range(start2, end2+1))
    return bool(elf1 & elf2)


def main() -> None:
    with open('input.txt') as f:
        input_data = f.read()
    input_data = input_data.strip().split('\n')
    input_data = [x.replace('-', ',').split(',') for x in input_data]
    input_data = [[int(x) for x in pair] for pair in input_data]

    is_subsets = [is_subset(*pair) for pair in input_data]
    print(sum(is_subsets))

    is_overlaps = [is_overlap(*pair) for pair in input_data]
    print(sum(is_overlaps))


if __name__ == '__main__':
    main()
