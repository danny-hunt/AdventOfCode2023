import sys
from days import *
import days

if __name__ == '__main__':
    print("Beginning Python execution...")
    timespan = range(1, 26)
    if len(sys.argv) > 1:
        day = int(sys.argv[1:][0])
        timespan = range(day, day + 1)
    for i in timespan:
        day_module = globals()[f'day{i:02}']
        day_module.part_one()
        day_module.part_two()
    print('Completed Python execution.')