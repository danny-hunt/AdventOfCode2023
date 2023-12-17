from utils.timing import timer
from utils.parsing import input_data
from functools import lru_cache


def parser(input: list[str]) -> list[str]:
    """
    abc     gda
    def --> heb
    ghi     ifc
    
    """
    return [''.join(list(i))[::-1] for i in zip(*input)]
    # return [''.join(list(i))[::-1] for i in zip(*input)]


@lru_cache(maxsize=None)
@timer(14)
def part_one():
    input = input_data(14, str)
    transposed_input = parser(input)
    total_total = 0
    for column in transposed_input:
        # print(column)
        col_total = 0
        no_of_spheres = 0
        for i, char in enumerate(column):
            value = i + 1
            if char == 'O':
                no_of_spheres += 1
            if char == "#":
                col_total += sum(range(value - 1, value - no_of_spheres - 1, -1))
                no_of_spheres = 0
            elif i == len(column) - 1:
                # print('sum', sum(range(value, value - no_of_spheres, -1)))
                col_total += sum(range(value, value - no_of_spheres, -1))
                no_of_spheres = 0
            # print(char, value, no_of_spheres)
        # print(col_total)
        total_total += col_total
    return total_total


@lru_cache(maxsize=None)
def evaluate(grid: list[list[str]]) -> int:
    str_grid = [''.join(row) for row in grid]
    transposed_grid = parser(str_grid)
    total_total = 0
    for column in transposed_grid:
        # print(column)
        col_total = 0
        no_of_spheres = 0
        for i, char in enumerate(column):
            value = i + 1
            if char == 'O':
                no_of_spheres += 1
            if char == "#":
                col_total += sum(range(value - 1, value - no_of_spheres - 1, -1))
                no_of_spheres = 0
            elif i == len(column) - 1:
                # print('sum', sum(range(value, value - no_of_spheres, -1)))
                col_total += sum(range(value, value - no_of_spheres, -1))
                no_of_spheres = 0
            # print(char, value, no_of_spheres)
        # print(col_total)
        total_total += col_total
    return total_total


@lru_cache(maxsize=None)
def rotate_clockwise(grid: tuple[tuple[str, ...], ...]) -> tuple[tuple[str, ...], ...]:
    return tuple((tuple(i) for i in zip(*grid[::-1])))


@lru_cache(maxsize=None)
def roll_north(grid: tuple[tuple[str, ...], ...]) -> tuple[tuple[str, ...], ...]:
    """
    abc     gda
    def --> heb
    ghi     ifc
    """
    rotated = rotate_clockwise(grid)
    output_rows: list[list[str]] = []
    for row in rotated:
        output_row = ['.'] * len(row)
        no_of_spheres = 0
        for i, char in enumerate(row):
            if char == 'O':
                no_of_spheres += 1
            if char == "#":
                output_row[i] = "#"
                for j in range(i - 1, i - no_of_spheres - 1, -1):
                    output_row[j] = "O"
                no_of_spheres = 0
            elif i == len(row) - 1:
                for j in range(i, i - no_of_spheres, -1):
                    output_row[j] = "O"
        output_rows.append(output_row)
    tuple_output =  tuple(tuple(i) for i in output_rows)
    return rotate_clockwise(rotate_clockwise(rotate_clockwise(tuple_output)))


@lru_cache(maxsize=None)
def rolled_evaluate(grid: tuple[tuple[str, ...], ...]) -> int:
    size = len(grid)
    total = 0
    for i, row in enumerate(grid):
        for char in row:
            if char == "O":
                total += size - i
    return total


@timer(14)
def part_two() -> int:
    # one_result = part_one()
    input: tuple[tuple[str, ...], ...] = tuple(input_data(14, tuple))
    sizes = set()

    for i in range(129):
        for _ in range(4):
            input = roll_north(input)
            input = rotate_clockwise(input)
        score = rolled_evaluate(input)
        if score not in sizes:
            # print("New score found at ", i, ": ", score)
            pass
        sizes.add(score)

        # if 150 > i >= 116:
        #     print(i, ": ", score)
        # Observe repeating pattern modulo 13
        # 999_999_999 - 128 = 0 mod 13
        # so answer is the same as after 128 iterations
    return rolled_evaluate(input)
