from dataclasses import dataclass
from typing import Callable
from utils.timing import timer
from utils.parsing import input_data
from functools import lru_cache


@dataclass
class Deet:
    dest_range_start: int
    source_range_start: int
    range_length: int


def generate_map_fn(deets: list[Deet]) -> Callable[[int], int]:
    def map_fn(val: int) -> int:
        for deet in deets:
            if val >= deet.source_range_start and val < deet.source_range_start + deet.range_length:
                return deet.dest_range_start + val - deet.source_range_start
        return val
    return map_fn


def parser(convert_map: str) -> Callable[[int], int]:
    _, data = convert_map.split(':\n')
    map_lines = data.split('\n')
    deets = [
        Deet(*map(int, line.split(' ')))
        for line in map_lines
    ]
    return generate_map_fn(deets)


@lru_cache(maxsize=None)
@timer(5)
def part_one():
    seed_string, *maps = input_data(5, str, sep='\n\n')
    _, *seeds = list(map(lambda x: int(x) if x != "seeds:" else None, seed_string.split(' ')))

    map_fns = list(map(parser, maps))

    resulting_positions = []
    for seed in seeds:
        for map_fn in map_fns:
            seed = map_fn(seed)
        resulting_positions.append(seed)

    return min(resulting_positions)

    

@timer(5)
def part_two():
    one_result = part_one()
    input = input_data(5, str)
    pass
