# https://adventofcode.com/2018/day/5

import string
import sys


def react(polymer):
    i = 0

    while i < len(polymer):
        try:
            if polymer[i].lower() == polymer[i+1].lower() and polymer[i] != polymer[i+1]:
                polymer = polymer[:i] + polymer[i+2:]
                if i > 0:
                    i -= 1
                continue
            i += 1
        except IndexError:
            break

    return polymer


INPUT = "input.txt" if len(sys.argv) == 1 else sys.argv[1]
print(f'Using input file "{INPUT}"')

with open(INPUT, "r") as f:
    data = f.readline().strip() # str


print('---- PT 1 ----')
print(len(react(data)))


print('---- PT 2 ----')
shortest_length = len(data)
for letter in string.ascii_lowercase:
    polymer = data.replace(letter, '').replace(letter.upper(), '')

    length = len(react(polymer))
    if shortest_length > length:
        shortest_length = length

print(shortest_length)
