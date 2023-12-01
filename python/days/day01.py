from utils.timing import timer
from utils.parsing import input_data
from functools import lru_cache
import re

# fouronevhnrz44
# eightg1
# 4ninejfpd1jmmnnzjdtk5sjfttvgtdqspvmnhfbm
# 78seven8
# 6pcrrqgbzcspbd

DIGITS = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

regex = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))')


WORD_OR_NUM_TO_NUM = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4, 
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}


@lru_cache(maxsize=None)
@timer(1)
def part_one():
    input = input_data(1)
    total = 0
    for line in input:
        first_digit = None
        last_digit = None
        for char in line:
            if char in DIGITS:
                if first_digit is None:
                    first_digit = char
                last_digit = char
        total += 10 * int(first_digit) + int(last_digit)
    return total
    

@timer(1)
def part_two():
    # one_result = part_one()
    total = 0
    for line in input_data(1):
        matches = regex.findall(line)
        total += 10 * WORD_OR_NUM_TO_NUM[matches[0]] + WORD_OR_NUM_TO_NUM[matches[-1]]
    return total
