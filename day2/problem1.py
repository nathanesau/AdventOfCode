# https://adventofcode.com/2019/day/2

OPCODE_ADD = 1
OPCODE_MULTIPLY = 2
OPCODE_FINISHED = 99

def solve(arr):
    arr[1] = 12 # 1202 state
    arr[2] = 2 # 1202 state
    for op_index in range(0, len(arr), 4):
        opcode = arr[op_index]

        if opcode is OPCODE_ADD:
            arr[arr[op_index + 3]] = arr[arr[op_index + 1]] + arr[arr[op_index + 2]]
        elif opcode is OPCODE_MULTIPLY:    
            arr[arr[op_index + 3]] = arr[arr[op_index + 1]] * arr[arr[op_index + 2]]
        elif opcode is OPCODE_FINISHED:
            return arr[0] # done
