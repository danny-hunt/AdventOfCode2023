from dataclasses import dataclass
from typing import Literal, Optional
from utils.timing import timer
from utils.parsing import input_data
from functools import lru_cache


def HASH(string: str) -> int:
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256
    return current_value


@lru_cache(maxsize=None)
@timer(15)
def part_one():
    input = input_data(15, str, ',')
    return sum(map(HASH, input))
    

@dataclass
class Lens:
    label: str
    focal_length: int


def insert_lens(box: list[Lens], lens: Lens) -> list[Lens]:
    for i, other_lens in enumerate(box):
        if other_lens.label == lens.label:
            box[i] = lens
            return box
    box.append(lens)
    return box


@timer(15)
def part_two() -> int:
    input = input_data(15, str, ',')
    boxes: list[list[Lens]] = [list() for _ in range(256)]

    for instruction in input:
        op_char = "-" if instruction[-1] == "-" else "="
        if op_char == "=":
            label = instruction[:-2 ]
            focal_length = int(instruction[-1])
            label_hash = HASH(label)
            new_lens = Lens(label, focal_length)
            insert_lens(boxes[label_hash], new_lens)
        else:
            label = instruction[:-1]
            label_hash = HASH(label)
            boxes[label_hash] = [lens for lens in boxes[label_hash] if lens.label != label]
    total = 0
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            total += lens.focal_length * (i + 1) * (j + 1)

    return total




    
