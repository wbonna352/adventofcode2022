def index_after_n_unique_chars(n: int, input_str: str) -> int:
    i = n
    while len(set(input_str[i-n:i])) < n:
        i += 1
    return i


def main() -> None:
    with open('input.txt', 'r') as f:
        input_data = f.read()

    print('Part one: ', index_after_n_unique_chars(4, input_data))
    print('Part two: ', index_after_n_unique_chars(14, input_data))


if __name__ == '__main__':
    main()
