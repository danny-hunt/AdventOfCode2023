from utils.timing import timer
from utils.parsing import input_data
from functools import lru_cache


def extrapolate_value(input: list[int]) -> int:
    layers = [input]
    should_continue = True
    while should_continue:
        last_layer = layers[-1]
        new_layer = [t - s for s, t in zip(last_layer, last_layer[1:])]
        if new_layer[0] == 0 and new_layer[-1] == 0:
            should_continue = False
        layers.append(new_layer)
    return sum(map(lambda x: x[-1], layers))


def extrapolate_back_value(input: list[int]) -> int:
    layers = [input]
    should_continue = True
    while should_continue:
        last_layer = layers[-1]
        new_layer = [t - s for s, t in zip(last_layer, last_layer[1:])]
        if new_layer[0] == 0 and new_layer[-1] == 0:
            should_continue = False
        layers.append(new_layer)
    total = 0
    for i, layer in enumerate(layers):
        total += layer[0] * (1 if i % 2 == 0 else -1)
    return total



@lru_cache(maxsize=None)
@timer(9)
def part_one():
    input = input_data(9, lambda x: list(map(int, x.split())))
    return sum(map(extrapolate_value, input))
    

@timer(9)
def part_two():
    input = input_data(9, lambda x: list(map(int, x.split())))
    return sum(map(extrapolate_back_value, input))
