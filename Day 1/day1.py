from aocd import get_data, transforms

data = get_data(day=1, year=2022)
lines = [l.split('\n') for l in data.split('\n\n')]

elves = sorted([sum(int(v) for v in v) for v in lines], reverse=True)

print(elves[0])
print(sum(elves[:3]))

