# https://adventofcode.com/2018/day/6

import sys
from collections import namedtuple
from pprint import pprint


Coord = namedtuple('Coord', 'x y')

def manhattan_distance(c1, c2):
    return abs(c1.x - c2.x) + abs(c1.y - c2.y)


def unique_min(lst, key=None):
    min_two = sorted(lst, key=key)[:2]

    if not key:
        key = lambda x: x

    if len(min_two) == 1 or key(min_two[0]) < key(min_two[1]):
        return min_two[0]

    return None


def area_is_infinite(grid, owner, min_x, max_x, min_y, max_y):
    for c in (tile_coord for tile_coord, belongs_to in grid.items() if belongs_to == owner):
        if c.x in [0, max_x] or c.y in [0, max_y]:
            return True

    return False


INPUT = "input.txt" if len(sys.argv) == 1 else sys.argv[1]
print(f'Using input file "{INPUT}"')

coords = []
with open(INPUT, "r") as f:
    lines = [line.strip() for line in f.readlines()]
    for line in lines:
        xy = [int(c) for c in line.split(', ')]
        coords.append(Coord(*xy))

max_x = max(c.x for c in coords)
min_x = min(c.x for c in coords)
max_y = max(c.x for c in coords)
min_y = max(c.x for c in coords)

grid = {
    Coord(x, y): None
    for x in range(max_x + 1)
    for y in range(max_y + 1)
}

hotspots = []

for tile in grid:
    # distances = [(A, 2), (B, 10), (C, 3), ...]
    distances = [(c, manhattan_distance(c, tile)) for c in coords]
    closest = unique_min(distances, key=lambda x: x[1])
    if closest:
        grid[tile] = closest[0]

    # pt2
    summed_distances = sum(distance for owner, distance in distances)
    if summed_distances < 10000:
        hotspots.append(summed_distances)

owners_with_finite_areas = [
    owner for owner in coords if not area_is_infinite(grid, owner, min_x, max_x, min_y, max_y)
]

largest_area = 0
for owner in owners_with_finite_areas:
    area = len([tile for tile_coord, belongs_to in grid.items() if belongs_to == owner])
    if area > largest_area:
        largest_area = area

print('\n---- PT 1 ----')
print(f'largest area: {largest_area}')

print('\n---- PT 2 ----')
print(f'hotspot area: {len(hotspots)}')
