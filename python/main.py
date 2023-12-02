import sys
import traceback
from days import *


if __name__ == '__main__':
    print("Beginning Python execution...")
    timespan = range(1, 26)
    if len(sys.argv) > 1:
        day = int(sys.argv[1:][0])
        timespan = range(day, day + 1)
    for i in timespan:
        try:
            day_module = globals()[f'day{i:02}']
            day_module.part_one()
            day_module.part_two()
        except FileNotFoundError:
            print(f'No input file found for day {i:02}.')
            break
        except Exception as e:
            print(f'Error executing day {i:02}: {e}')
            print(traceback.format_exc())
            break
    print('Python execution ended.')