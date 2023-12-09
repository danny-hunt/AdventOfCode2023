from utils.timing import timer
from utils.parsing import input_data
from functools import lru_cache, reduce
import math


def parser(input: str) -> list[int]:
    _, data = input.split(':')
    return list(map(int, data.split()))


def win_race(total_time: int, time_held: int, distance: int) -> bool:
    return ((total_time - time_held) * time_held) > distance

@lru_cache(maxsize=None)
@timer(6)
def part_one():
    times, distances = input_data(6, parser)
    win_count_per_race = []
    for time, distance in zip(times, distances):
        win_count_per_race.append(len(list(filter(bool, (win_race(time, t, distance) for t in range(time + 1))))))
    # return product of win counts
    return reduce(lambda x, y: x * y, win_count_per_race)


@timer(6)
def part_two():
    times, distances = input_data(6, parser)
    time = int(''.join(map(str, times)))
    distance = int(''.join(map(str, distances)))
    
    # t^2 - time * t + distance = 0
    a = 1
    b = -time
    c = distance
    t_one = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    t_two = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    return math.floor(t_one) - math.ceil(t_two) + 1
