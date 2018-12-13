INPUT = "input.txt"

with open(INPUT, "r") as f:
    # initial_state = f.readline().strip("initial_state: ").strip()

    # Your puzzle input contains a list of pots from 0 to the right
    # and whether they do (#) or do not (.) currently contain a plant, the initial state.
    # For example, an initial state of #..##.... indicates that pots 0, 3, and 4 currently contain plants.

    lines = f.readlines()


initial_state = lines[0].split(": ")[1].strip()
rules = {}
empty = "....."

for line in lines[2:]: # skip the \n
    left, right = line.split(" => ")
    rules[left.strip()] = right.strip()


def plant_transformation(no_of_gen):
    current_gen = empty + initial_state + empty

    count = 0
    offset = 0

    for gen in range(no_of_gen):
        next_state = current_gen

        for i in range(len(current_gen)):
            symbol = current_gen[i: i + 5] # the symbol from the rules consists of 5 chars
            center = i + 2 # we need to change the center symbol

            if symbol in rules:
                next_state = next_state[:center] + rules[symbol] + next_state[center + 1:] # do the transformation

        current_gen = empty + next_state + empty
        offset += 5

        previous_count = 0 # for part 2
        count = 0
        # the pots are numbered, with 0 in front of you
        # to the left, the pots are numbered -1, -2, -3, and so on; to the right, 1, 2, 3
        # we need to find the sum of *the numbers* of all pots which contain a plant
        for i in range(len(current_gen)):
            pot = i - 5 - offset

            if current_gen[i] == "#":
                count += pot

        print(f"Generation {gen} - count {count} - difference {count - previous_count}")
    
    previous_count = count # for part 2
    return count


count = plant_transformation(20)
print(f"Part 1: {count}")


# After fifty billion (50000000000) generations, what is the sum of the numbers of all pots which contain a plant?
# let's try to see some patterns here
count = plant_transformation(1000)

# Generation 990 - count 51424 - difference 51424
# Generation 991 - count 51475 - difference 51475
# Generation 992 - count 51526 - difference 51526
# Generation 993 - count 51577 - difference 51577
# Generation 994 - count 51628 - difference 51628
# Generation 995 - count 51679 - difference 51679
# Generation 996 - count 51730 - difference 51730
# Generation 997 - count 51781 - difference 51781
# Generation 998 - count 51832 - difference 51832
# Generation 999 - count 51883 - difference 51883
# after a while, it converges to 51

converge = 51
mega_sum = (50000000000 - 1000) * converge + count
print(f"Part 2: {mega_sum}")