# https://adventofcode.com/2019/day/4

def is_valid_password(pwd):
    has_adjacent = False
    prev_digit = -1
    max_digit = -1
    for digit in pwd:
        digit = int(digit)
        if digit == prev_digit:
            has_adjacent = True
        if digit >= max_digit:
            max_digit = digit
        else:
            return False # digits need to be increasing
        prev_digit = digit
    return has_adjacent # increasing property already satisfied

def solve(prange):
    num_passwords = 0
    for i in range(prange[0], prange[1] + 1, 1):
        # only pass words of length 6 between prange
        if is_valid_password(str(i)):
            num_passwords += 1
    return num_passwords