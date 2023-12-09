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
def part_one() -> int:
    seed_string, *maps = input_data(5, str, sep='\n\n')
    _, *seeds = list(map(lambda x: int(x) if x != "seeds:" else None, seed_string.split(' ')))

    map_fns = list(map(parser, maps))

    resulting_positions = []
    for seed in seeds:
        for map_fn in map_fns:
            seed = map_fn(seed)
        resulting_positions.append(seed)

    return min(resulting_positions)


def overlaps(interval_1: tuple[int, int], interval_2: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int]] | None:
    # Return three tuples - the first is the start of interval_1 that doesnt overlap with interval_2
    # The second is the overlap between the two intervals
    # The third is the end of interval_1 that doesnt overlap with interval_2
    start_1, end_1 = interval_1
    start_2, end_2 = interval_2
    if start_1 > end_2 or start_2 > end_1:
        return None
    if start_1 < start_2:
        return (start_1, start_2), (start_2, min(end_1, end_2 )), (min(end_1, end_2), end_1)
    else:
        return (start_1, start_1), (start_1, min(end_1 , end_2)), (min(end_1, end_2), end_1)


def deets_parser(convert_map: str) -> list[Deet]:
    _, data = convert_map.split(':\n')
    map_lines = data.split('\n')
    deets = [
        Deet(*map(int, line.split(' ')))
        for line in map_lines
    ]
    return deets


def map_intervals_to_next(intervals: list[tuple[int, int]], deets: list[Deet]) -> list[tuple[int, int]]:
    output_intervals = []
    for interval in intervals:
        current_interval = interval
        for deet in sorted(deets, key=lambda x: x.source_range_start):
            overlapping_regions = overlaps(current_interval, (deet.source_range_start, deet.source_range_start + deet.range_length))
            if overlapping_regions:
                start_interval, overlap_interval, end_interval = overlapping_regions
                if start_interval[1] > start_interval[0]:
                    output_intervals.append(start_interval)
                if overlap_interval[1] > overlap_interval[0]:
                    output_intervals.append(
                        (deet.dest_range_start + overlap_interval[0] - deet.source_range_start, deet.dest_range_start + overlap_interval[1] - deet.source_range_start)
                    )
                current_interval = end_interval
        if current_interval[1] > current_interval[0]:
            output_intervals.append(current_interval)
    return output_intervals




@timer(5)
def part_two():
    seed_string, *maps = input_data(5, str, sep='\n\n')
    _, *seeds = list(map(lambda x: int(x) if x != "seeds:" else None, seed_string.split(' ')))
    seed_intervals = []
    for seed_start, range_length in zip(seeds[::2], seeds[1::2]):
        seed_intervals.append((seed_start, seed_start + range_length))
        
    mappings_list = list(map(deets_parser, maps))

    for deets in mappings_list:
        seed_intervals = map_intervals_to_next(seed_intervals, deets)

    print(len(seed_intervals))
    # print(seed_intervals)

    seed_intervals.sort(key=lambda x: x[0])
    print(seed_intervals[:10])

    min_value = min([interval[0] for interval in seed_intervals])
    print(min_value)

    # for interval in seed_intervals:
    #     for map_fn in map_fns:
    #         interval = (map_fn(interval[0]), map_fn(interval[1]))

    # resulting_positions = []
    # for seed in seeds:
    #     for map_fn in map_fns:
    #         seed = map_fn(seed)
    #     resulting_positions.append(seed)

    return min_value
