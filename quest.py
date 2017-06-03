import random

'''
Elementy składowe:

1. NPC
named
2. Name
seeks a company of adventurers
3. To do what




ddsd
dsadasd
asdasdsa
sadsad
'''

with open('theme.txt', 'r') as file:
    dataTheme = file.read().splitlines()
print('Main Theme: ', random.choice(dataTheme))

with open('opponent.txt', 'r') as file:
    dataOpponent = file.read().splitlines()
print('Opponent: ', random.choice(dataOpponent))
