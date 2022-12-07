
from collections import defaultdict
from itertools import zip_longest
from aocd import get_data, transforms

import hypothesis
import hypothesis.strategies as st
import pytest
import re
import pdb

data = get_data(day=7, year=2022)

