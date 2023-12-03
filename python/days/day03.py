from typing import NamedTuple
from utils.timing import timer
from utils.parsing import input_data
from functools import lru_cache
from itertools import count


SYMBOLS = {"*", "+", "&", "=", "$", "%", "/", "#", "-", "@"}


def get_neighbours(coords: tuple[int, int]) -> set[tuple[int, int]]:
    x, y = coords
    return {
        (x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
        (x, y - 1), (x, y + 1),
        (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)
    }


def get_block_neighbours(coords:set[tuple[int, int]]) -> set[tuple[int, int]]:
    neighbours = set()
    for coord in coords:
        neighbours.update(get_neighbours(coord))
    return neighbours.difference(coords)




@lru_cache(maxsize=None)
@timer(3)
def part_one() -> int:
    input = input_data(3, str)
    symbol_locations: set[tuple[int, int]] = set()
    total = 0
    for i, line in enumerate(input):
        for j, char in enumerate(line):
            if char in SYMBOLS:
                symbol_locations.add((i, j))

    for i, line in enumerate(input):
        current_number = ""
        current_block = set()
        for j, char in enumerate(line):
            if char.isdigit():
                current_number += char
                current_block.add((i, j))
            elif current_number:
                # resolve number
                if get_block_neighbours(current_block).intersection(symbol_locations):
                    total += int(current_number)
                current_number = ""
                current_block = set()
        # resolve number
        if get_block_neighbours(current_block).intersection(symbol_locations):
            total += int(current_number)
        current_number = ""
        current_block = set()
    return total


class PartNumber(NamedTuple):
    id: int
    value: int


id_counter = count(start=1)
def get_id():
    return next(id_counter)


@timer(3)
def part_two() -> int:
    input = input_data(3, str)
    gear_locations: set[tuple[int, int]] = set()
    total = 0
    for i, line in enumerate(input):
        for j, char in enumerate(line):
            if char is '*':
                gear_locations.add((i, j))

    part_numbers: dict[tuple[int, int], PartNumber] = {}

    for i, line in enumerate(input):
        current_number = ""
        current_block = set()
        num_id = get_id()
        for j, char in enumerate(line):
            if char.isdigit():
                current_number += char
                current_block.add((i, j))
            elif current_number:
                # resolve number
                for coords in current_block:
                    part_numbers[coords] = PartNumber(num_id, int(current_number))
                current_number = ""
                current_block = set()
                num_id = get_id()
        # resolve number
        for coords in current_block:
            part_numbers[coords] = PartNumber(num_id, int(current_number))
        current_number = ""
        current_block = set()
        num_id = get_id()

    for gear in gear_locations:
        gear_neighbours = get_neighbours(gear)
        gear_part_numbers = set(
            part_numbers[neighbour]
            for neighbour in gear_neighbours
            if neighbour in part_numbers
        )
        if len(gear_part_numbers) > 2:
            raise ValueError(f"Gear {gear} has more than 2 neighbours: {gear_part_numbers}")
        elif len(gear_part_numbers) == 2:
            total += gear_part_numbers.pop().value * gear_part_numbers.pop().value
        else:
            # print("Unpaired gears")
            pass

    return total
