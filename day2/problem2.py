# https://adventofcode.com/2019/day/2#part2

OPCODE_ADD = 1
OPCODE_MULTIPLY = 2
OPCODE_FINISHED = 99

def get_output(arr, noun, verb):
    arr[1] = noun
    arr[2] = verb
    for op_index in range(0, len(arr), 4):
        opcode = arr[op_index]

        if opcode is OPCODE_ADD:
            arr[arr[op_index + 3]] = arr[arr[op_index + 1]] + arr[arr[op_index + 2]]
        elif opcode is OPCODE_MULTIPLY:    
            arr[arr[op_index + 3]] = arr[arr[op_index + 1]] * arr[arr[op_index + 2]]
        elif opcode is OPCODE_FINISHED:
            return arr[0] # done

    return arr[0] # should not happen

def solve(arr, target):
    computed = {}
    max_noun = min(99, len(arr) - 1)
    max_verb = min(99, len(arr) - 1)
    for noun in range(0, max_noun):
        for verb in range(0, max_verb):
            pair = (arr[noun], arr[verb]) if arr[noun] < arr[verb] else (arr[verb], arr[noun])
            if pair not in computed:
                output = get_output(arr.copy(), noun, verb)
                computed[pair] = output
                if output == target:
                    return 100 * noun + verb
    return -1 # no result found
    
