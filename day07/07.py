import sys
from pprint import pprint
from collections import defaultdict


INPUT = "input.txt" if len(sys.argv) == 1 else sys.argv[1]
print(f'Using input file "{INPUT}"')

   
parent_steps = {}
child_steps = {}

SECONDS = 60
WORKERS = 5

with open(INPUT) as f:
    # "Step C must be finished before step A can begin."

    for line in f:
        words = line.split() # ["Step", "C", ...]
        parent = words[1]
        child = words[-3]

        if child in parent_steps:
            parent_steps[child].append(parent)
        else: # KeyError
            parent_steps[child] = [parent]

        if parent in child_steps:
            child_steps[parent].append(child)
        else:
            child_steps[parent] = [child]

        if parent not in parent_steps:
            parent_steps[parent] = []

print(parent_steps)
print("----------")
print(child_steps)

order = []

try:
    while True:
        for step in sorted(parent_steps.keys()):
            if not parent_steps[step]:
                order.append(step)
                del parent_steps[step]
                for child in child_steps[step]:
                    parent_steps[child].remove(step)
                del child_steps[step]
                break
except KeyError:
    pass

output = "".join(order)
print(output)

