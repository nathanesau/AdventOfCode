# https://adventofcode.com/2019/day/5#part2

import common.intcode as intcode

def solve(arr, input_parameter):
    ans = intcode.IntCode(arr, [input_parameter]).execute()
    return(ans)
