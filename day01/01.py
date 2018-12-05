# https://adventofcode.com/2018/day/1

INPUT = "input.txt"

with open(INPUT, "r") as input_file:
    arr = [int(line.rstrip("\n")) for line in input_file]

f = 0
for el in arr:
    f = f + el
print(f"Frequency: {f}")


def cycle(arr):
    f = 0
    seen = set([0]) # because of [+1 -1]
    while True:
        for el in arr:
            f = f + el
            if f in seen:
                return f
            seen.add(f)

seen = cycle(arr)
print(f"Seen frequencies: {seen}")
