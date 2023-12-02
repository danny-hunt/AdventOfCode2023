from utils.timing import timer
from utils.parsing import input_data
from functools import lru_cache


@lru_cache(maxsize=None)
@timer(6)
def part_one():
    input = input_data(6, str)
    pass
    

@timer(6)
def part_two():
    one_result = part_one()
    input = input_data(6, str)
    pass
