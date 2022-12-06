from collections import defaultdict
from itertools import zip_longest
from aocd import get_data, transforms
import re

data = get_data(day=6, year=2022)

for i in range(14, len(data)-14):
    if len(set(data[i-14:i])) == 14:
        print(i)
        break



