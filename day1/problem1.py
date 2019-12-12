# https://adventofcode.com/2019/day/1

def fuel_required_module(module_mass):
    return module_mass // 3 - 2

def solve(arr):
    fuel_requirement = 0
    for module_mass in arr:
        fuel_requirement += fuel_required_module(module_mass)
    return fuel_requirement
