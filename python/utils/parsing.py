from pathlib import Path
from typing import Callable, Optional, TypeVar, cast 


def day_str(day: int) -> str:
    "Return the day number as a zero-padded string."
    return f'{day:02}'


T = TypeVar('T')


def input_data(day: int, parser: Optional[Callable[[str], T]], sep='\n') -> list[T]:
    "Split the day's input file into sections separated by `sep`, and apply `parser` to each."
    if parser is None:
        parser = lambda x: cast(T, x)
    script_dir=Path(__file__).parent.parent.parent 
    file_name=(script_dir / f'inputs/{day_str(day)}.in').resolve()

    with open(file_name) as f:
        sections = f.read().rstrip().split(sep)
        return list(map(parser, sections))
