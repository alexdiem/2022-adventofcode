def read_config():
    with open('./data/day5_config') as f:
        stacks = [[] for i in range(9)]
        for line in f.readlines():
            conf = []
            for i in range(len(stacks)):
                s = line[(i*4):(i*4)+4].strip()
                if s:
                    if s.startswith('['):
                        stacks[i].insert(0, s[1])

    return stacks


def read_instructions():
    with open('./data/day5_instructions') as f:
        instructions = []
        for line in f.readlines():
            inst = line.split()
            amount = int(inst[1])
            movefrom = int(inst[3])
            moveto = int(inst[5])
            instructions.append([amount, movefrom, moveto])
        return instructions
                



def partone():
    stacks = read_config()
    instructions = read_instructions()

    for inst in instructions:
        amount, movefrom, moveto = inst
        for i in range(amount):
            elem = stacks[movefrom-1].pop()
            stacks[moveto-1].append(elem)
    return ''.join([stack[-1] for stack in stacks])


def parttwo():
    pass


if __name__ == "__main__":
    print("The solution to part one is: ", partone())
    print("The solution to part two is: ", parttwo())