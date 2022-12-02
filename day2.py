from aocd import get_data, transforms
from collections import defaultdict
data = get_data(day=2, year=2022)
lines = transforms.lines(data)

lines = [(p[0], p[2]) for p in lines]
# A, X : Rock
# B, Y: Paper
# C, Z: Scissors

shape = {'A': 1, 'B': 2, 'C': 3}
h = {'X': 'A', 'Y': 'B', 'Z': 'C'}
win_con = {('C', 'A'), ('B', 'C'), ('A', 'B')}
p2_con = {
    ('A', 'X') : ('A', 'C'),
    ('A', 'Y') : ('A', 'A'),
    ('A', 'Z') : ('A', 'B'),
    ('B', 'X') : ('B', 'A'),
    ('B', 'Y') : ('B', 'B'),
    ('B', 'Z') : ('B', 'C'),
    ('C', 'X') : ('C', 'B'),
    ('C', 'Y') : ('C', 'C'),
    ('C', 'Z') : ('C', 'A'),
}

# Rock, Paper, Scissors
# A, B, C


# Win Conditions : Rock < Paper, Paper < Scissors, Scissors < Rock
#                  A < B, B < C, C < A
#


# Win Condition: Player 2 is one index to the right
# Lose Condition: Player 1 is one index to the left
# Draw Condition: Same Index

# 3 + 1 is 4
# 4 % 3 is 1

def score_game(lines, part_2=False):
    score = 0
    for p1, p2 in lines:
        if not part_2:
            p2 = h[p2]
        else:
            (p1, p2) = p2_con[(p1, p2)]

        if p1 == p2:
            score += shape[p2] + 3
        elif (p1, p2) in win_con:
            score += 6 + shape[p2]
        else:
            score += shape[p2]
    return score


p1 = score_game(lines)
p2 = score_game(lines, True)


print(f'Part One: {p1}')
print(f'Part Two: {p2}')
