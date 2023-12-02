from utils.timing import timer
from utils.parsing import input_data
from functools import lru_cache


@lru_cache(maxsize=None)
@timer(16)
def part_one():
    input = input_data(16, str)
    pass
    

@timer(16)
def part_two():
    one_result = part_one()
    input = input_data(16, str)
    pass
