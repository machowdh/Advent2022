from aocd import get_data, transforms
import re

data = get_data(day=4, year=2022)
lines = transforms.lines(data)

ranges = [list(map(int, re.sub(r'(-)|(,)', ' ', line).split())) for line in lines]
pairs = [sorted([r[:2], r[2:]]) for r in ranges]

part_one = 0
part_two = 0

for pair in pairs:
    x, y = pair
    if y[0] <= x[1]:
        part_two += 1
    if (x[0] < y[0] and y[1] <= x[1]) or (x[0] == y[0] and y[1] >= x[1]):
        part_one += 1

print(f'Part One: {part_one}')
print(f'Part Two: {part_two}')


