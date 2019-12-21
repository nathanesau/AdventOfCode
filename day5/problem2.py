# https://adventofcode.com/2019/day/5#part2

POSITION_MODE = 0
IMMEDIATE_MODE = 1

OPCODE_ADD = 1
OPCODE_MULTIPLY = 2
OPCODE_INPUT = 3
OPCODE_OUTPUT = 4
OPCODE_JUMPIFTRUE = 5
OPCODE_JUMPIFFALSE = 6
OPCODE_LESSTHAN = 7
OPCODE_EQUALS = 8
OPCODE_FINISHED = 99

NUM_ARGUMENTS = {OPCODE_ADD: 3,
                 OPCODE_MULTIPLY: 3,
                 OPCODE_INPUT: 1, 
                 OPCODE_OUTPUT : 1,
                 OPCODE_JUMPIFTRUE: 2,
                 OPCODE_JUMPIFFALSE: 2,
                 OPCODE_LESSTHAN: 3,
                 OPCODE_EQUALS: 3,
                 OPCODE_FINISHED: 0}
        
class Argument:
    def __init__(self, address, value):
        self.address = address
        self.value = value
        
class IntCodeCPU:
    def __init__(self, arr, input):
        self.arr = arr
        self.input = input
        self.output = None
        self.halted = False
        self.op_index = 0

    def get_arguments(self, modes):
        arguments = []
        for i in range(len(modes)): # Note: some modes may be skipped
            value = self.arr[self.op_index + i + 1]
            if int(modes[i]) == IMMEDIATE_MODE:
                arguments.append(Argument(value, value))
            else: # POSITION_MODE
                arguments.append(Argument(value, self.arr[value]))
        return arguments

    def execute_instruction(self, opcode, arguments): # return next op_index
        if opcode is OPCODE_ADD:
            self.arr[arguments[2].address] = arguments[0].value + arguments[1].value
            return self.op_index + NUM_ARGUMENTS[opcode] + 1
        elif opcode is OPCODE_MULTIPLY:
            self.arr[arguments[2].address] = arguments[0].value * arguments[1].value
            return self.op_index + NUM_ARGUMENTS[opcode] + 1
        elif opcode is OPCODE_INPUT:
            self.arr[arguments[0].address] = self.input
            return self.op_index + NUM_ARGUMENTS[opcode] + 1
        elif opcode is OPCODE_OUTPUT:
            self.output = arguments[0].value
            return self.op_index + NUM_ARGUMENTS[opcode] + 1
        elif opcode is OPCODE_JUMPIFTRUE:
            # do not modify self
            return arguments[1].value if arguments[0].value != 0 else self.op_index + NUM_ARGUMENTS[opcode] + 1
        elif opcode is OPCODE_JUMPIFFALSE:
            # do not modify self
            return arguments[1].value if arguments[0].value == 0 else self.op_index + NUM_ARGUMENTS[opcode] + 1
        elif opcode is OPCODE_LESSTHAN:
            self.arr[arguments[2].address] = int(arguments[0].value < arguments[1].value)
            return self.op_index + NUM_ARGUMENTS[opcode] + 1
        elif opcode is OPCODE_EQUALS:
            self.arr[arguments[2].address] = int(arguments[0].value == arguments[1].value)
            return self.op_index + NUM_ARGUMENTS[opcode] + 1
        elif opcode is OPCODE_FINISHED:
            self.halted = True
            return None

    def execute(self):
        last_output = None
        while not self.halted: # keep updating output until halt
            opcode = self.arr[self.op_index] % 100
            modes = str(self.arr[self.op_index]).zfill(5)[:3][::-1]
            arguments = self.get_arguments(modes[:NUM_ARGUMENTS[opcode]])
            self.op_index = self.execute_instruction(opcode, arguments)
            if opcode == OPCODE_OUTPUT:
                last_output = self.output
        return last_output

def solve(arr, input):
    cpu = IntCodeCPU(arr, input)
    ans = cpu.execute()
    return(ans)
