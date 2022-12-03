import string


PRIOS = {k: v for k, v in zip(string.ascii_letters, range(1,26*2+1))}

def partone():
    with open('./data/day3') as f:
        total = 0
        for line in f.readlines():
            l = int(len(line)/2)
            comp1 = line[:l]
            comp2 = line[l:]
            for letter in comp1:
                if letter in comp2:
                    total += PRIOS[letter]
                    break
    return total


def parttwo():
    return None


if __name__ == "__main__":
    print("The solution to part one is: ", partone())
    print("The solution to part two is: ", parttwo())