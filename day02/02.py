# https://adventofcode.com/2018/day/2

from collections import Counter

INPUT = "input2.txt"

def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]


with open(INPUT, "r") as input_file:
    arr = [line.rstrip("\n") for line in input_file]

twos = 0
threes = 0
for el in arr:
    cnt = Counter(el)
    if 2 in cnt.values():
        twos += 1
    if 3 in cnt.values():
        threes +=1

m = twos * threes
print(m)


# levenshtein
from itertools import combinations

combs = combinations(arr, 2)
for comb in combs:
    if levenshtein(comb[0], comb[1]) == 1:
        break

solution = ""
pairs = zip(comb[0], comb[1])
for pair in pairs:
    if pair[0] == pair[1]:
        solution += pair[0]

print(solution)
