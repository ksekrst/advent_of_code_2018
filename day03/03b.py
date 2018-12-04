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

    return claim_id, int(x), int(y), int(width), int(height) # strings


matrix = [[0 for i in range(1000)] for j in range(1000)]
overlap = 0

claims = {} # {claim_id: set(tiles)}
tiles = {(x, y): set() for x in range(1000) for y in range(1000)} # {tile_coords: set(claims)}

with open(INPUT, "r") as f:
    for line in f:
        y = line.split("\n") # arrays
        l = ("".join(y)) # convert to strings

        claim_id, x, y, width, height = parse(l)
        claims[claim_id] = set()
        # print(x, y, width, height)
        
        for i in range(x, x+width):
            for j in range(y, y+height):
                matrix[i][j] += 1 # fill with ones

                claims[claim_id].add((i, j)) # add a tile to the set of tiles belonging to the current claim
                tiles[(i, j)].add(claim_id) # add a claim to the set of claims having the right to the current tile

                if matrix[i][j] == 2: # collision detection
                    overlap += 1

# print(overlap)

dirty_tiles = set(tile_coords for tile_coords, claims in tiles.items() if len(claims) > 1)
for claim_id, tiles in claims.items():
    if not any(tile in dirty_tiles for tile in tiles):
        print(f"Good claim: {claim_id}")

# for x in [matrix, claims, tiles]:
    # print(sys.getsizeof(x))