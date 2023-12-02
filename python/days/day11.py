from utils.timing import timer
from utils.parsing import input_data
from functools import lru_cache


@lru_cache(maxsize=None)
@timer(11)
def part_one():
    input = input_data(11, str)
    pass
    

@timer(11)
def part_two():
    one_result = part_one()
    input = input_data(11, str)
    pass
