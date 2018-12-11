SERIAL_NUMBER = 3214 # serial number
GRID_SIZE = 300
SQUARE_SIZE = 3


def test_power_level():
    assert power_level(122, 79, 57) == -5
    assert power_level(217, 196, 39) == 0
    assert power_level(101, 153, 71) == 4


def test_largest_total_power():
    serial_number = 42
    grid = fuel_grid(serial_number)
    ltp, _ = largest_square(grid, serial_number, 3)
    assert ltp == (21, 61), f'Got {ltp}'


def power_level(x, y, serial_number):
    """Find the power level of a cell"""

    rack_id = x + 10 # find the fuel cell's rack ID, which is its X coordinate plus 10
    power_level = rack_id * y # begin with a power level of the rack ID times the Y coordinate
    power_level += serial_number # increase the power level by the value of the grid serial number (your puzzle input)
    power_level *= rack_id # set the power level to itself multiplied by the rack ID.

    # keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0)
    power_level = str(power_level) # to find the length
    if len(power_level) > 2:
        digit = int(power_level[-3])
    else:
       digit = 0
    digit -= 5 # subtract 5 from the power level

    return digit


def fuel_grid(serial_number):
    """Create a grid, fill it with zeroes, then fill it with coordinates."""

    grid = []

    for i in range(GRID_SIZE):
        grid.append([])
        for j in range(GRID_SIZE):
            grid[i].append(power_level(i+1, j+1, serial_number))

    return grid


def largest_square(grid, serial_number, square_size):
    """Your goal is to find the 3x3 square which has the largest total power.
    The square must be entirely within the 300x300 grid.
    Identify this square using the X,Y coordinate of its top-left fuel cell."""

    largest_total_power = 0
    top_left = (1,1)

    for i in range (GRID_SIZE - square_size):
        for j in range(GRID_SIZE - square_size):
            total = 0
            for x in range(square_size):
                for y in range(square_size):
                    total += grid[i+x][j+y]

            if total > largest_total_power:
                largest_total_power = total
                top_left = (i+1, j+1)
   
    return top_left, largest_total_power


def largest_square_all_sizes(grid, serial_number):
    """Find a square of any size with largest total power"""

    largest_total_power = 0
    largest_power_size = 0
    largest_top_left = (1, 1)

    for size in range(1, 50):
        top_left, total_power = largest_square(grid, serial_number, size)
        if total_power > largest_total_power:
            largest_total_power = total_power
            largest_power_size = size
            largest_top_left = top_left
    
    return largest_top_left, largest_power_size


if __name__ == "__main__":
    test_power_level()
    test_largest_total_power()

    grid = fuel_grid(SERIAL_NUMBER)
    
    coords, largest_total_power = largest_square(grid, SERIAL_NUMBER, SQUARE_SIZE)
    print(f"Part 1 coordinates: {coords}")
    
    any_coords, size = largest_square_all_sizes(grid, SERIAL_NUMBER)
    print(f"Part 2 coordinates: {any_coords}, {size}")

