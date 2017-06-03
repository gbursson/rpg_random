import random

with open('theme.txt', 'r') as file:
    dataTheme = file.read().splitlines()
print('Main Theme: ', random.choice(dataTheme))


with open('opponent.txt', 'r') as file:
    dataOpponent = file.read().splitlines()
print('Opponent: ', random.choice(dataOpponent))
