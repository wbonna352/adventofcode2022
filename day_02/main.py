with open('input.txt', 'r') as f:
    input_data = f.read()


def points_counter(game: tuple[str, str]) -> int:

    points_for_shape = {'X': 1, 'Y': 2, 'Z': 3}
    points_for_result = {'win': 6, 'draw': 3, 'loss': 0}

    def game_result() -> str:
        if game in (('A', 'X'), ('B', 'Y'), ('C', 'Z')):
            return 'draw'
        elif game in (('A', 'Y'), ('B', 'Z'), ('C', 'X')):
            return 'win'
        else:
            return 'loss'

    outcome = game_result()

    return points_for_shape.get(game[1]) + points_for_result.get(outcome)


def points_counter2(game: tuple[str, str]) -> int:

    def input_encoder() -> tuple[str, str]:
        if game in (('A', 'X'), ('B', 'Z'), ('C', 'Y')):
            encoded_shape = 'Z'
        elif game in (('A', 'Z'), ('B', 'Y'), ('C', 'X')):
            encoded_shape = 'Y'
        else:
            encoded_shape = 'X'

        return game[0], encoded_shape

    encoded_input = input_encoder()

    return points_counter(encoded_input)


input_data = input_data.strip().split('\n')
input_data = [tuple(game.split(' ')) for game in input_data]

# part one
points1 = [points_counter(game) for game in input_data]
sum_of_points1 = sum(points1)
print(f'{sum_of_points1=}')

# part two
points2 = [points_counter2(game) for game in input_data]
sum_of_points2 = sum(points2)
print(f'{sum_of_points2=}')
