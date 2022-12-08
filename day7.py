
from collections import defaultdict, deque
from itertools import zip_longest
from aocd import get_data, transforms
from aocd.models import Puzzle
from aocd import submit


import hypothesis
import hypothesis.strategies as st
import pytest
import re
import pdb

data = get_data(day=7, year=2022)
puzzle = Puzzle(year=2022, day=7)


commands = [line.split() for line in transforms.lines(data)]
file_system = defaultdict(int)
path = []

for command in commands:
    if command[1] == 'cd':
        if command[2] == '..':
            path.pop()
        else:
            path.append(command[2])
    elif command[1] == 'ls':
        continue
    elif command[0] == 'dir':
        continue
    else:
        size = int(command[0])
        for i in range(1, len(path) + 1):
            file_system['/'.join(path[:i])] += size

print(*file_system.items(), sep='\n')

part_one = 0
part_two = 10**9

need_to_free = file_system['/'] - (70000000 - 30000000)

for k, v in file_system.items():
    if v <= 100000:
        part_one += v
    if v >= need_to_free:
        part_two = min(part_two, v)

# submit(part_one, part='a', day=7, year=2022)
# submit(part_two, part='b', day=7, year=2022)
