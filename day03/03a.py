# https://adventofcode.com/2018/day/3
import sys

INPUT = "input3.txt" if len(sys.argv) == 1 else sys.argv[1]
print(f'Using input file "{INPUT}"')


def parse(line):
    """Parses a given input line,
    for example: #1258 @ 544,52: 19x29"""
    
    claim_id, at, position, size = line.split() # split by spaces
    #print(f"Claim: {claim_id}, position: {position}, size: {size}")

    x, y = position.split(",")
    y = y[:-1] # remove the ":"
    #print(f"x: {x}, y: {y}")

    width, height = size.split("x")
    #print(f"width: {width}, height: {height}")

    return int(x), int(y), int(width), int(height) # strings


matrix = [[0 for _ in range(1000)] for _ in range(1000)]
overlap = 0

with open(INPUT, "r") as f:
    for line in f:
        y = line.split("\n") # arrays
        l = ("".join(y)) # convert to strings

        x, y, width, height = parse(l)
        # print(x, y, width, height)
        
        for i in range(width):
            for j in range(height):
                matrix[x+i][y+j] += 1 # fill zeroes with ones if the squares are taken
                if matrix[x+i][y+j] == 2: # collision detection
                    overlap += 1

print(overlap)
