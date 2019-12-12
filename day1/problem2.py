# https://adventofcode.com/2019/day/1#part2

def fuel_required_module(module_mass):
    fuel = module_mass // 3 - 2
    if fuel <= 0:
        return 0 
    return fuel + fuel_required_module(fuel)

def solve(arr):
    fuel_requirement = 0
    for module_mass in arr:
        fuel_requirement += fuel_required_module(module_mass)
    return fuel_requirement
