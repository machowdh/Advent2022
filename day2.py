from aocd import get_data, transforms
from collections import defaultdict, namedtuple

data = get_data(day=2, year=2022)
lines = transforms.lines(data)

state = ['A', 'B', 'C']

class Game:
    
    def __init__(self, char):
        self.char = char
        state_index = state.index(char)

        self.wins = state[state_index - 1]
        self.loses = state[(state_index + 1) % 3]
        self.value = state_index + 1

    def __eq__(self, other):
        return self.char == other

    def __repr__(self):
        return f'{self.char}'

def score_game(lines, part_2=False):
    score = 0
    for p1, _, p2 in lines:
        player_one = Game(p1)
        if part_2:
            if p2 == 'X':
                player_two = Game(player_one.loses)
            elif p2 == 'Y':
                player_two = Game(player_one.wins)
            else:
                player_two = Game(player_one)
        else:
            player_two = Game(chr(ord(p2) - 23))
        score += player_two.value
        if player_one == player_two:
            score += 3
        elif player_two.wins == player_one.char:
            score += 6
    return score

p1 = score_game(lines)
p2 = score_game(lines, True)


print(f'Part One: {p1}')
print(f'Part Two: {p2}')
