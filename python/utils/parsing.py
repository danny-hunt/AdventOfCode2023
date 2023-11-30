
def day_str(day: int) -> str:
    "Return the day number as a zero-padded string."
    return f'{day:02}'


def input_data(day: int, parser=str, sep='\n') -> list:
    "Split the day's input file into sections separated by `sep`, and apply `parser` to each."
    # If file does not exist, return empty list
    file_name = f'../inputs/{day_str(day)}.in'
    try:
        with open(file_name) as f:
            sections = f.read().rstrip().split(sep)
            return list(map(parser, sections))
    except FileNotFoundError:
        return []

    