from utils.timing import timer
from utils.parsing import input_data
from functools import lru_cache


def parser(input: str) -> tuple[str, tuple[int, ...]]:
    placements, num_str = input.split()
    nums = tuple(map(int, num_str.split(",")))
    return (placements, nums)


@lru_cache(maxsize=2048)
def solve_part(placements: str, nums: tuple[int]) -> int:
    min_length = sum(nums) + len(nums) - 1
    space_length = len(placements)
    total = 0
    if len(nums) == 0:
        if placements.count("#") == 0:
            return 1
        else:
            return 0
    first_hash = placements.find("#")
    for i in range(0, min(first_hash if first_hash >= 0 else 999, space_length - min_length) + 1):
        if i + nums[0] < len(placements) and placements[i + nums[0]] == "#":
            continue
        for j in range(i, i + nums[0]):
            if placements[j] == ".":
                break
        else:
            total += solve_part(placements[(i + nums[0] + 1):], nums[1:])
    return total


@lru_cache(maxsize=None)
@timer(12)
def part_one():
    #?#??#??????????.??.? 7,2,3,1
    input = input_data(12, parser)
    answers = list(map(lambda x: solve_part(*x), input))
    return sum(answers)


def unfold_parser(input: str) -> tuple[str, tuple[int, ...]]:
    placements, nums = parser(input)
    return '?'.join([placements for _ in range(5)]), 5 * nums


@timer(12)
def part_two():
    input = input_data(12, unfold_parser)
    answers = list(map(lambda x: solve_part(*x), input))
    return sum(answers)
    