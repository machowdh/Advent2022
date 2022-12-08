
from collections import defaultdict, deque
from itertools import zip_longest
from aocd import get_data, transforms
from functools import reduce

import hypothesis
import hypothesis.strategies as st
import pytest
import re
import pdb

data = get_data(day=11, year=2021)

octopi = transforms.lines(data)


def turn():
    visited = [[False for _ in range(10)] for _ in range(10)]
    
    q = deque([(i, j) for i in range(10) for j in range(10)])

    while q:
        x, y = q.popleft()
        v