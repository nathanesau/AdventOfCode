# https://adventofcode.com/2019/day/3

def get_visited_squares(path):
    visited = {} # store number of steps to this point
    prev_coord = [0, 0]
    prev_steps = 0
    for move in path:
        direction = move[0]
        amount = int(move[1:])
        if direction == 'U':
            for y in range(prev_coord[1], prev_coord[1] + amount + 1, 1):
                visited[(prev_coord[0], y)] = abs(y - prev_coord[1]) + prev_steps
            new_coord = [prev_coord[0], prev_coord[1] + amount]
        if direction == 'D':
            for y in range(prev_coord[1], prev_coord[1] - amount - 1, -1):
                visited[(prev_coord[0], y)] = abs(y - prev_coord[1]) + prev_steps
            new_coord = [prev_coord[0], prev_coord[1] - amount]
        if direction == 'L':
            for x in range(prev_coord[0], prev_coord[0] - amount - 1, -1):
                visited[(x, prev_coord[1])] = abs(x - prev_coord[0]) + prev_steps
            new_coord = [prev_coord[0] - amount, prev_coord[1]]
        if direction == 'R':
            for x in range(prev_coord[0], prev_coord[0] + amount + 1, 1):
                visited[(x, prev_coord[1])] = abs(x - prev_coord[0]) + prev_steps
            new_coord = [prev_coord[0] + amount, prev_coord[1]]
        prev_coord = new_coord
        prev_steps = prev_steps + abs(amount)
    return visited

def mdistance(point1, point2):
    return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])

def solve(path1, path2):
    visited1 = get_visited_squares(path1)
    visited2 = get_visited_squares(path2)

    steps_closest = float('Inf')
    for square1 in visited1:
        if square1 == (0, 0): # skip
            continue
        if square1 in visited2: # intersection
            steps_square1 = visited1[square1] + visited2[square1]
            if steps_square1 < steps_closest:
                steps_closest = steps_square1

    return steps_closest