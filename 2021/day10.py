
from collections import defaultdict
from itertools import zip_longest
from aocd import get_data, transforms
from functools import reduce

import hypothesis
import hypothesis.strategies as st
import pytest
import re
import pdb

data = get_data(day=10, year=2021)

corrupted_lines = transforms.lines(data)

closing =  {'}':'{',
            ']':'[',
            ')':'(' ,
            '>':'<'}
opening = {'(':')', '<':'>', '{':'}','[':']'}
score = {')': 3, ']': 57, '}': 1197, '>':25137}

points = 0
incomplete_indices = set()
for idx, corrupted_line in enumerate(corrupted_lines):
    # pdb.set_trace()
    stack = []
    for i, char in enumerate(corrupted_line):
        if char not in closing:
            stack.append(char)
        elif not stack and char in closing or stack and closing[char] != stack[-1]:
            # pdb.set_trace()
            points += score[char]
            incomplete_indices.add(idx)
            break
        else:
            stack.pop()

incomplete = [corrupted_lines[idx] for idx, corrupted_line in enumerate(corrupted_lines) if idx not in incomplete_indices]

scores = []
ac = {')': 1, ']':2, '}':3, '>':4}
for inc in incomplete:
    stack = []
    for i, c in enumerate(inc):
        if c not in closing:
            stack.append(c)
        elif stack and stack[-1] == closing[c]:
            stack.pop()
    v = 0
    while stack:
        v = v * 5 + ac[opening[stack.pop()]]
    scores.append(v)
scores.sort()
N = len(scores)

print(scores[N//2])



