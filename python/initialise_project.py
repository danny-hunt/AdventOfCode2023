
if __name__ == '__main__':
    for i in range(1, 26):
        # Make file ./days/XX.py
        # Each file contains functions for part 1 and part 2
        # Each function should be decorated with @timer
        with open(f'./days/day{i:02}.py', 'w') as f:
            f.write(f'''from utils.timing import timer
from utils.parsing import input_data
from functools import lru_cache


@lru_cache(maxsize=None)
@timer({i})
def part_one():
    input = input_data({i})
    pass
    

@timer({i})
def part_two():
    one_result = part_one()
    input = input_data({i})
    pass
''')
                    

    print('Hello World!')