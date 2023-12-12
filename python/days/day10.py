from collections import Counter
from time import sleep
from typing import Literal, cast
from utils.timing import timer
from utils.parsing import input_data
from functools import lru_cache


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


pipes = {
    "F": {"down", "right"},
    "L": {"up", "right"},
    "7": {"down", "left"},
    "J": {"up", "left"},
    "|": {"up", "down"},
    "-": {"left", "right"},
}


invert_direction = {
    "up": "down",
    "down": "up",
    "left": "right",
    "right": "left"
}


@lru_cache(maxsize=None)
@timer(10)
def part_one() -> float:
    input = input_data(10, lambda x: list(x))
    start: tuple[int, int]
    for i, row in enumerate(input):
        for j, val in enumerate(row):
            if val == 'S':
                start = (i, j)
                # Found by hand what the S should be replaced with
                input[i][j] = '|'
    position = start
    came_from = "up"
    no_of_steps = 0
    while position != start or no_of_steps == 0:
        i, j = position
        for direction in pipes[input[i][j]]:
            if direction != came_from:
                position = (i + directions[direction][0], j + directions[direction][1])
                came_from = invert_direction[direction]
                break
        no_of_steps += 1
    return no_of_steps / 2


StepType = Literal['|', '7', 'F', 'J', 'L']
    

@timer(10)
def part_two() -> int:
    input = input_data(10, lambda x: list(x))
    start: tuple[int, int]
    for i, row in enumerate(input):
        for j, val in enumerate(row):
            if val == 'S':
                start = (i, j)
                # Found by hand what the S should be replaced with
                input[i][j] = '|'
    position = start
    came_from = "up"
    no_of_steps = 0
    loop_positions: set[tuple[int, int, StepType]] = {(*position, '|')}
    while position != start or no_of_steps == 0:
        i, j = position
        loop_positions.add((*position, cast(StepType, input[i][j])))
        for direction in pipes[input[i][j]]:
            if direction != came_from:
                position = (i + directions[direction][0], j + directions[direction][1])
                came_from = invert_direction[direction]
                break
        no_of_steps += 1

    total_in_loop = 0
    # TODO: determine the internals from the loop_positions(?)
    for i in range(140):
        for j in range(140):
            if (i, j, input[i][j]) in loop_positions:
                continue
            loop_positions_to_left = {l for l in loop_positions if l[0] == i and l[1] < j}
            loop_kinds = Counter(l[2] for l in loop_positions_to_left)
            sum = loop_kinds['|'] + min(loop_kinds['7'], loop_kinds['L']) + min(loop_kinds['F'], loop_kinds['J'])
            if sum % 2 == 1:
                total_in_loop += 1
            # |
            # L7
            # JF

    return total_in_loop
