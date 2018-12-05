# https://adventofcode.com/2018/day/5

import sys

INPUT = "input.txt" if len(sys.argv) == 1 else sys.argv[1]
print(f'Using input file "{INPUT}"')


with open(INPUT, "r") as f:
    data = f.readline().strip() # str

    i = 0
    while i < len(data):
        try:
            if data[i].lower() == data[i+1].lower() and data[i] != data[i+1]:
                data = data[:i] + data[i+2:] 
                if i > 0:
                    i -= 1
                continue
            i += 1
        except IndexError:
            break

    print(len(data))
