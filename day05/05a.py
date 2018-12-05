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
                i = i - 2 # remove the index by 2 to the left when an adjacent pair has been deleted
                continue
            i += 1
        except IndexError: # check if i > 0
            break

    print(len(data))
