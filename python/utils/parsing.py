from pathlib import Path 


def day_str(day: int) -> str:
    "Return the day number as a zero-padded string."
    return f'{day:02}'


def input_data(day: int, parser=str, sep='\n') -> list:
    "Split the day's input file into sections separated by `sep`, and apply `parser` to each."
    script_dir=Path(__file__).parent.parent.parent 
    file_name=(script_dir / f'inputs/{day_str(day)}.in').resolve()

    with open(file_name) as f:
        sections = f.read().rstrip().split(sep)
        return list(map(parser, sections))
    