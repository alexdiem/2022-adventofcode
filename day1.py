def partone():
    max = 0
    cal = 0
    with open('data/day1') as f:
        for line in f.readlines():
            line = line.strip()
        
            if line == "":
                if cal > max:
                    max = cal
                cal = 0
            else:
                cal += int(line)

    return max


def parttwo():
    return None


if __name__ == "__main__":
    print("The solution to part one is: ", partone())
    print("The solution to part two is: ", parttwo())