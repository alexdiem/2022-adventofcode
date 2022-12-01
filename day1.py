from math import inf


def get_topelf(top=inf):
    max = 0
    cal = 0
    with open('data/day1') as f:
        for line in f.readlines():
            line = line.strip()
        
            if line == "":
                if cal > max and cal < top:
                    max = cal
                cal = 0
            else:
                cal += int(line)

    return max


def partone():
    return get_topelf()


def parttwo():
    total = 0
    top = inf
    for i in range(3):
        top = get_topelf(top)
        total += top
    return total


if __name__ == "__main__":
    print("The solution to part one is: ", partone())
    print("The solution to part two is: ", parttwo())