from utils.timing import timer
from utils.parsing import input_data
from functools import lru_cache
from dataclasses import dataclass


@dataclass
class CubeSet:
    red: int
    green: int
    blue: int


@dataclass
class Game:
    id: int
    sets: list[CubeSet]
    

def parser(input: str) -> Game:
    sets = []
    game_string, trial_sets = input.split(":")
    _, game_id_str = game_string.split()
    game_id = int(game_id_str)
    for trial_set in trial_sets.split(";"):
        colors = trial_set.split(",")
        red = 0
        green = 0
        blue = 0
        for color_string in colors:
            count, color = color_string.strip().split()
            if color == "red":
                red = int(count)
            elif color == "green":
                green = int(count)
            elif color == "blue":
                blue = int(count)
            else:
                raise ValueError(f"Unknown color: {color}")
        cube_set = CubeSet(red, green, blue)
        sets.append(cube_set)
    return Game(game_id, sets)


def is_valid_cube_set(cube_set: CubeSet) -> bool:
    MAX_RED, MAX_GREEN, MAX_BLUE = 12, 13, 14
    return cube_set.red <= MAX_RED and cube_set.green <= MAX_GREEN and cube_set.blue <= MAX_BLUE


@lru_cache(maxsize=None)
@timer(2)
def part_one():
    games: list[Game] = input_data(2, parser=parser)
    successful_id_total = 0
    for game in games:
        if not all(is_valid_cube_set(cube_set) for cube_set in game.sets):
            continue
        successful_id_total += game.id
    return successful_id_total
    

@timer(2)
def part_two():
    games: list[Game] = input_data(2, parser=parser)
    total = 0
    for game in games:
        min_red = max(cube_set.red for cube_set in game.sets)
        min_green = max(cube_set.green for cube_set in game.sets)
        min_blue = max(cube_set.blue for cube_set in game.sets)
        cube_power = min_red * min_green * min_blue
        total += cube_power
    return total
