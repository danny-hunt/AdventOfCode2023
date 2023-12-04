from dataclasses import dataclass
from typing import TypedDict
from utils.timing import timer
from utils.parsing import input_data
from functools import lru_cache


@dataclass
class Card:
    numbers: list[int]
    winning_numbers: list[int]


def parser(line: str) -> Card:
    card_deets = line.split(": ")[1]
    winning_number_str, number_str = card_deets.split(" | ")
    winning_numbers = list(map(int, 
                               filter(bool, winning_number_str.strip().split())))
    numbers = list(map(int, filter(bool, number_str.strip().split())))
    return Card(numbers, winning_numbers)


class CardTwo(TypedDict):
    numbers: list[int]
    winning_numbers: list[int]
    count: int


def parser_two(line: str) -> CardTwo:
    card_deets = line.split(": ")[1]
    winning_number_str, number_str = card_deets.split(" | ")
    winning_numbers = list(map(int, 
                               filter(bool, winning_number_str.strip().split())))
    numbers = list(map(int, filter(bool, number_str.strip().split())))
    return {"numbers": numbers, "winning_numbers": winning_numbers, "count": 1}


@lru_cache(maxsize=None)
@timer(4)
def part_one():
    input = input_data(4, parser)
    total = 0
    for card in input:
        winning_count = len(list(filter(lambda x: x in card.numbers, card.winning_numbers)))
        if winning_count:
            total += 2**(winning_count - 1)
    return total
    

@timer(4)
def part_two():
    # one_result = part_one()
    input = input_data(4, parser_two)
    length = len(input)
    for i, card in enumerate(input):
        winning_count = len(list(filter(lambda x: x in card["numbers"], card["winning_numbers"])))
        if winning_count:
            for j in range(i + 1, i + 1 + winning_count):
                if j < length:
                    input[j]["count"] += card["count"]
    return sum(card["count"] for card in input)
