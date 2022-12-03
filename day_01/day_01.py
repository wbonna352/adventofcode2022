with open('input.txt', 'r') as f:
    input_data = f.read()


def sum_from_list_of_str(x: list[str]) -> int:
    return sum([int(i) for i in x])


def sum_of_max_3(x: list[int]) -> int:
    return sum(sorted(x, reverse=True)[:3])


input_data = input_data.split('\n\n')
input_data = [elf.strip().split('\n') for elf in input_data]
input_data = [sum_from_list_of_str(elf) for elf in input_data]

elf_max_value = max(input_data)
sum_of_max_3_elves = sum_of_max_3(input_data)


print(f'{elf_max_value=}')
print(f'{sum_of_max_3_elves=}')
