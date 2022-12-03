from aocd import get_data, transforms
from functools import reduce
import string

data = get_data(day=3, year=2022)


lines = transforms.lines(data)
groups = [lines[i:i+3] for i in range(0, len(lines), 3)]
char_value = {c: i for i, c in enumerate(string.ascii_letters, start=1)}

print(f'Part One: {sum(char_value[(set(l[:len(l)//2]) & set(l[len(l)//2:])).pop()] for l in lines)}')
print(f'Part Two: {sum(char_value[reduce(lambda x, y : set(x) & set(y), g).pop()] for g in groups)}')
