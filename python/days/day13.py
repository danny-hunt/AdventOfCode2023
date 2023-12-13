from dataclasses import dataclass
from utils.timing import timer
from utils.parsing import input_data
from functools import lru_cache


def parser(input: str) -> list[str]:
    return input.split()


@dataclass
class PotentialMatch:
    value: int
    stack: list[str]


def get_horizontal_line_values(grid: list[str], multiplier: int = 1) -> int:
    total = 0
    rows_seen: list[str] = []
    potential_matches: list[PotentialMatch] = []
    for j, row in enumerate(grid):
        for match in potential_matches:
            if row == match.stack.pop():
                if len(match.stack) == 0:
                    total += match.value * multiplier
                    potential_matches.remove(match)
                else:
                    # match survives with 1 fewer row
                    pass
            else:
                # match dies
                potential_matches.remove(match)
        if rows_seen and row == rows_seen[-1]:
            # new match
            potential_matches.append(
                PotentialMatch(j, [*rows_seen[:-1]])
            )
            if potential_matches[-1].stack == []:
                total += potential_matches[-1].value * multiplier
                potential_matches.pop()
        rows_seen.append(row)
        print(potential_matches)
    for match in potential_matches:
        total += match.value * multiplier
    return total


def transpose_grid(grid: list[str]) -> list[str]:
    return [''.join(list(i)) for i in zip(*grid)]
    # for i, row in enumerate(grid):
    #     for j, val in enumerate(row):

    # return [
    #     "".join([row[i] for row in grid])
    #     for i in range(len(grid[0]))
    # ]


@lru_cache(maxsize=None)
@timer(13)
def part_one() -> int:
    input = input_data(13, parser, sep="\n\n")
    total_total = 0
    print(transpose_grid(input[0]))
    for grid in input:
        total = 0
        total += get_horizontal_line_values(grid, 100)
        total += get_horizontal_line_values(transpose_grid(grid), 1)
        total_total += total  
    return total_total  


def compare_rows(row_a: str, row_b: str) -> int:
    return sum([0 if a == b else 1 for a, b in zip(row_a, row_b)])


def get_new_reflection_value(grid: list[str]) -> int:
    for i in range(1, len(grid)):
        no_of_rows_to_compare = min(i, len(grid) - i)
        total_comparison = 0
        for j in range(no_of_rows_to_compare):
            no_of_row_diffs = compare_rows(grid[i - 1 - j], grid[i + j])
            total_comparison += no_of_row_diffs
            if total_comparison > 1:
                break
        if total_comparison == 1:
            return i * 100
    
    transposed_grid = transpose_grid(grid)
    for i in range(1, len(transposed_grid)):
        no_of_rows_to_compare = min(i, len(transposed_grid) - i)
        total_comparison = 0
        for j in range(no_of_rows_to_compare):
            no_of_row_diffs = compare_rows(transposed_grid[i - 1 - j], transposed_grid[i + j])
            total_comparison += no_of_row_diffs
            if total_comparison > 1:
                break
        if total_comparison == 1:
            return i * 1
    raise Exception("No smudged reflection found")


@timer(13)
def part_two():
    input = input_data(13, parser, sep="\n\n")
    total = 0 
    for grid in input:
        total += get_new_reflection_value(grid)
    return total
