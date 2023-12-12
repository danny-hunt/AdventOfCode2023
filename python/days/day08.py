from utils.timing import timer
from utils.parsing import input_data
from functools import lru_cache, reduce
import re
import math


def find_three_letter_sequences(string: str) -> tuple[str, str, str]:
    # regex for three capital letters in a row
    return re.findall(r'[A-Z]{3}', string)


def determine_steps(start_position: str, instructions: str, map: dict[str, tuple[str, str]], part: int = 1) -> int:
    position = start_position
    steps = 0
    continue_ = True
    while continue_:
        for letter in instructions:
            steps += 1
            left, right = map[position]
            if letter == 'L':
                position = left
            else:
                position = right
            if position == 'ZZZ' or part == 2 and position.endswith('Z'):
                continue_ = False
                break
    return steps


@lru_cache(maxsize=None)
@timer(8)
def part_one():
    instructions, rest = input_data(8, str, sep='\n\n')
    map = {}
    for path in rest.split('\n'):
        origin, left, right = find_three_letter_sequences(path)
        map[origin] = (left, right)
        # print(origin, left, right)
    # paths = list(map(parser, rest.split('\n')))
    return determine_steps('AAA', instructions, map)
    

@timer(8)
def part_two():
    instructions, rest = input_data(8, str, sep='\n\n')
    directions = {}
    for path in rest.split('\n'):
        origin, left, right = find_three_letter_sequences(path)
        directions[origin] = (left, right)
    
    ghost_starts = [key for key in directions if key[2] == 'A']
    print(ghost_starts)
    return math.lcm(*map(lambda x: determine_steps(x, instructions, directions, 2), ghost_starts))
    # return reduce(lambda x, y: x*y, list(map(lambda x: determine_steps(x, instructions, directions, 2), ghost_starts)))
