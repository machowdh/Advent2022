
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

data = get_data(day=8, year=2022)

trees = [list(map(int, l)) for l in transforms.lines(data)]

m, n = len(trees), len(trees[0])

visible = 0


top = [[trees[i][j] for j in range(n)] for i in range(m)]
bottom = [[trees[i][j] for j in range(n)] for i in range(m)]
left = [[trees[i][j] for j in range(n)] for i in range(m)]
right = [[trees[i][j] for j in range(n)] for i in range(m)]





for j in range(n):
    for i in range(m):
        if i == 0:
            top[i][j] = trees[i][j]
        else:
            top[i][j] = max(top[i-1][j], trees[i][j])

for j in range(n):
    for i in reversed(range(m - 1)):
        bottom[i][j] = max(bottom[i + 1][j], trees[i][j])


for i in range(m):
    for j in range(1, n):
        left[i][j] = max(left[i][j - 1], trees[i][j])

for i in range(m):
    for j in reversed(range(n - 1)):
        right[i][j] = max(right[i][j + 1], trees[i][j])



def nge(arr):
    stack = []
    res = [0] * len(arr)
    for i, v in enumerate(arr):
        while stack and v >= stack[-1][1]:
            idx, _ = stack.pop()
            res[idx] = i - idx
        stack.append((i, v))
    return res



for i in range(m):
    for j in range(n):
        if i == 0 or j == 0 or i == m - 1 or j == n -1:
            visible += 1
        else:
            vt = trees[i][j] > top[i - 1][j]
            vb = trees[i][j] > bottom[i + 1][j]
            vl = trees[i][j] > left[i][j - 1]
            vr = trees[i][j] > right[i][j + 1]
            visible += int(vt or vb or vl or vr)
r = 0
for i in range(n):
    for j in range(m):
        vd = []
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni = i + dx
            nj = j + dy
            c = 0
            v = True
            while ni in range(n) and nj in range(m):
                if trees[ni][nj] >= trees[i][j]:
                    v = False
                    break
                ni += dx
                nj += dy
                c += 1
            vd.append(c + (1 if ni in range(n) and nj in range(m) else 0))
        r = max(r, vd[0]*vd[1]*vd[2]*vd[3])

print(r)
