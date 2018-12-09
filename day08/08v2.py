import sys
from pprint import pprint


INPUT = "input.txt" if len(sys.argv) == 1 else sys.argv[1]
print(f'Using input file "{INPUT}"')


def parse(nums):
    """ pt. 1 """
    nchildren = nums[0] # number of children
    nmeta = nums[1] # number of metadata
    offset = 2 # step in each iteration
    total = 0 # sum of metadata

    for i in range(nchildren):
        new_offset, smeta = parse(nums[offset:]) # move
        offset += new_offset
        total += smeta
    
    metadata = nums[offset:(offset+nmeta)]
    offset += nmeta
    total += sum(metadata)

    return offset, total


def parse_root(nums):
    """ pt. 2 """
    nchildren = nums[0] # number of children
    nmeta = nums[1] # number of metadata
    offset = 2
    total = 0

    child_meta = {}

    for i in range(1, nchildren+1):
        new_offset, smeta = parse_root(nums[offset:]) # move
        child_meta[i] = smeta
        offset += new_offset

    metadata = nums[offset:(offset+nmeta)]

    if nchildren == 0:
        total += sum(metadata)
    else:
        for pointer in metadata:
            if pointer in child_meta:
                total += child_meta[pointer]

    offset += nmeta

    return offset, total


with open(INPUT) as f:
    nums = [int(x) for x in f.read().split() if x]

print('---- PT 1 ----')
_, total = parse(nums)
print(total)

print('---- PT 2 ----')
_, value = parse_root(nums)
print(value)
