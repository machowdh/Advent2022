
from collections import defaultdict
from itertools import zip_longest
from aocd import get_data, transforms
from functools import reduce

import hypothesis
import hypothesis.strategies as st
import pytest
import re
import pdb

data = get_data(day=9, year=2021)

heightmap = [list(map(int, line)) for line in transforms.lines(data)]

m = len(heightmap)
n = len(heightmap[0])

part_one = 0

def neighbors(x, y):
    for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
        if 0 <= nx < m and 0 <= ny < n:
            yield nx, ny


low_points = []
for x in range(m):
    for y in range(n):
        if all(heightmap[x][y] < heightmap[nx][ny] for nx, ny in neighbors(x, y)):
            low_points.append((x, y))
            part_one += heightmap[x][y] + 1

print(part_one)


visited = [[False for _ in range(n)] for _ in range(m)]

def dfs(x, y):
    visited[x][y] = True
    size = 1
    for nx, ny in neighbors(x, y):
        if not visited[nx][ny] and heightmap[nx][ny] > heightmap[x][y] and heightmap[nx][ny] != 9:
            visited[nx][ny] = True
            size += dfs(nx, ny)
    return size

sizes = []

for x, y in low_points:
    if not visited[x][y]:
        sizes.append(dfs(x, y))

print(reduce(lambda x, y : x * y, sorted(sizes)[-3:]))



        
