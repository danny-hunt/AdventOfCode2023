from utils.timing import timer
from utils.parsing import input_data
from functools import lru_cache
from itertools import combinations


@lru_cache(maxsize=None)
@timer(11)
def part_one() -> int:
    input = input_data(11, str)
    galaxies: set[tuple[int, int]] = set()
    galaxies_by_row: dict[int, set[int]] = {i: set() for i in range(140)}
    galaxies_by_col: dict[int, set[int]] = {i: set() for i in range(140)}
    for i, row in enumerate(input):
        for j, val in enumerate(row):
            if val == "#":
                galaxies_by_row[i].add(j)
                galaxies_by_col[j].add(i)
                galaxies.add((i, j))
    empty_rows = {i for i in range(140) if len(galaxies_by_row[i]) == 0}
    empty_cols = {i for i in range(140) if len(galaxies_by_col[i]) == 0}
    total = 0
    for gal_a, gal_b in combinations(galaxies, 2):
        distance = abs(gal_a[0] - gal_b[0]) + abs(gal_a[1] - gal_b[1])
        for i in range(min(gal_a[0], gal_b[0]) + 1, max(gal_a[0], gal_b[0])):
            if i in empty_rows:
                distance += 1
        for i in range(min(gal_a[1], gal_b[1]) + 1, max(gal_a[1], gal_b[1])):
            if i in empty_cols:
                distance += 1
        total += distance
    return total


@timer(11)
def part_two():
    input = input_data(11, str)
    galaxies: set[tuple[int, int]] = set()
    galaxies_by_row: dict[int, set[int]] = {i: set() for i in range(140)}
    galaxies_by_col: dict[int, set[int]] = {i: set() for i in range(140)}
    for i, row in enumerate(input):
        for j, val in enumerate(row):
            if val == "#":
                galaxies_by_row[i].add(j)
                galaxies_by_col[j].add(i)
                galaxies.add((i, j))
    empty_rows = {i for i in range(140) if len(galaxies_by_row[i]) == 0}
    empty_cols = {i for i in range(140) if len(galaxies_by_col[i]) == 0}
    total = 0
    for gal_a, gal_b in combinations(galaxies, 2):
        distance = abs(gal_a[0] - gal_b[0]) + abs(gal_a[1] - gal_b[1])
        for i in range(min(gal_a[0], gal_b[0]) + 1, max(gal_a[0], gal_b[0])):
            if i in empty_rows:
                distance += 999999
        for i in range(min(gal_a[1], gal_b[1]) + 1, max(gal_a[1], gal_b[1])):
            if i in empty_cols:
                distance += 999999
        total += distance
    return total
