from aocd import get_data, transforms

data = get_data(day=1, year=2022)
lines = [l.split('\n') for l in data.split('\n\n')]

elves = sorted([sum(list(map(int, e))) for e in lines])

print(f'Part One: {elves[-1]}')
print(f'Part Two: {sum(elves[-3:])}')

