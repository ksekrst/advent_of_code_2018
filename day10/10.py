import re
import sys
from collections import deque
from pprint import pprint

import numpy as np
from PIL import Image


class Point:
    rgx = re.compile(r'position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)')
    def __init__(self, x, y, vx=0, vy=0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    
    def advance(self, steps=1):
        self.x += self.vx
        self.y += self.vy
    
    @classmethod
    def from_input_line(cls, line):
        m = cls.rgx.match(line)
        x, y, vx, vy = map(lambda i: int(i), [m[1], m[2], m[3], m[4]])
        return Point(x, y, vx, vy)
    
    # def is_in_bounding_box(self, top_left, bottom_right):
    #     return top_left.x <= self.x <= bottom_right.x and top_left.y <= self.y <= bottom_right.y
    
    def __repr__(self):
        return f'<{self.__class__.__name__} at {hex(id(self))}: {self.__dict__}>'
    

def bounding_box(points):
    min_x = min(points, key=lambda p: p.x).x
    min_y = min(points, key=lambda p: p.y).y
    max_x = max(points, key=lambda p: p.x).x
    max_y = max(points, key=lambda p: p.y).y

    return Point(min_x, min_y), Point(max_x, max_y)


def bounding_box_area(points):
    min_x = min(points, key=lambda p: p.x).x
    min_y = min(points, key=lambda p: p.y).y
    max_x = max(points, key=lambda p: p.x).x
    max_y = max(points, key=lambda p: p.y).y

    return (max_x - min_x) * (max_y - min_y)


# def draw(points, title):
#     # top_left, bottom_right = bounding_box(points)
#     # dx = bottom_right.x - top_left.x
#     # dy = bottom_right.y - top_left.y
#     # print(dx, dy)
#     grid = np.zeros((1000, 1000), dtype=int)
#     top_left, bottom_right = Point(-499, -499), Point(500, 500)
#     count = 0
#     for p in points:
#         if p.is_in_bounding_box(top_left, bottom_right):
#             # print(p, p.x - top_left.x, p.y - top_left.y)
#             grid[p.x - top_left.x, p.y - top_left.y] = 255
#             count += 1

#     if count == len(points):
#         print(f'{count} pixels found')
#         # print(sum(sum(grid)))
#         im = Image.fromarray(grid.transpose())
#         print(title)
#         im.show()
#         mod = input()
#         return int(mod)

def main(input_lines):
    points = [Point.from_input_line(line) for line in input_lines]
    pprint(points)

    # mod = 10
    # for t in range(100000):
    #     top_left, bottom_right = bounding_box(points)
    #     #pprint((top_left, bottom_right))
    #     if t % (mod or 1) == 0:
    #         mod = draw(points, str(t))
    #         # input()
    #     for p in points:
    #         p.advance()

    t = 0
    # we'll store the last 10 points configurations so that we can draw them
    history = deque(maxlen=10)
    top_left, bottom_right = bounding_box(points)
    # we'll store the width and height of the point "swarm" to compare them
    # between steps
    prev_size = (bottom_right.x - top_left.x, bottom_right.y - top_left.y)
    while True:
        # get new size
        top_left, bottom_right = bounding_box(points)
        dx = bottom_right.x - top_left.x
        dy = bottom_right.y - top_left.y

        # we can't just store the "points" list, we need to make a copy
        # (pointers, references, shallow copies etc.)
        history.append((t, [(p.x, p.y) for p in points]))

        # if we detect that the "swarm" has stopped shrinking
        # it might mean that the message has been shown so we'll end
        # the simulation
        if dx > prev_size[0] or dy > prev_size[1]:
            break

        # otherwise, carry on
        for point in points:
            point.advance()
        
        t += 1
        prev_size = (dx, dy)
    
    for time, snapshot in history:
        draw(time, snapshot, ascii=True)


def draw(time, snapshot, ascii=False):
    # we'll use a margin around the points for legibility reasons
    margin = 10

    points = [Point(x, y) for x, y in snapshot]
    top_left, bottom_right = bounding_box(points)
    dx = bottom_right.x - top_left.x + 2*margin
    dy = bottom_right.y - top_left.y + 2*margin
    
    pixels = np.zeros((dx+1, dy+1), dtype=int)

    for p in points:
        pixels[p.x - top_left.x + margin, p.y - top_left.y + margin] = 255
    
    # pixels = pixels.transpose()

    print(f'time: {time}s, image size: {dx - 2*margin}x{dy -2*margin}')
    if ascii:
        for row in range(dy):
            chars = []
            for col in range(dx):
                chars.append('#' if pixels[col, row] == 255 else ' ')
            print(''.join(chars))
    else:
        im = Image.fromarray(pixels.transpose())
        im.show()


if __name__ == '__main__':
    INPUT = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
    print(f'Using input file "{INPUT}"')

    with open(INPUT) as f:
        lines = [line.strip() for line in f.readlines()]
    
    sys.exit(main(lines))
    