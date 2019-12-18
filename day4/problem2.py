# https://adventofcode.com/2019/day/4#part2

def is_valid_password(pwd):
    adjacent_counter = 0
    adjacent_nums = {}
    prev_digit = -1
    max_digit = -1
    for digit in pwd:
        digit = int(digit)
        if digit == prev_digit:            
            adjacent_counter += 1
            adjacent_nums[digit] = adjacent_counter
        else:
            adjacent_counter = 1
        if digit >= max_digit:
            max_digit = digit
        else:
            return False # digits need to be increasing
        prev_digit = digit
    if adjacent_nums:
        return 2 in adjacent_nums.values() # increasing property already satisfied
    else:
        return False

def solve(prange):
    num_passwords = 0
    for i in range(prange[0], prange[1] + 1, 1):
        # only pass words of length 6 between prange
        if is_valid_password(str(i)):
            num_passwords += 1
    return num_passwords