from collections import defaultdict
from itertools import zip_longest
from aocd import get_data, transforms
import re

data = get_data(day=5, year=2022)
lines = transforms.lines(data)
s = defaultdict(list)
stacks = lines[:9]
indices = [(i, c) for i, c in enumerate(stacks[-1]) if c.isdigit()]
for i, c in indices:
    s[int(c)] = [stack[i] for stack in stacks if stack[i].isalpha()][::-1]

for line in lines[10:]:
    c = re.sub(r'(move)|(from)|(to)', '', line)
    amount, start, end = list(map(int, c.split()))
    moved = [s[start].pop() for _ in range(amount)][::-1]
    s[end] += moved

print(''.join(v[-1] for v in s.values()))