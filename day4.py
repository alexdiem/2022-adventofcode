def range_string_to_int(s):
    return [int(num) for num in s.split('-')]


def partone():
    with open('./data/day4') as f:
        count = 0
        for line in f.readlines():
            elves = line.split(',')
            firstrange = range_string_to_int(elves[0])
            secondrange = range_string_to_int(elves[1])
            if (firstrange[0] <= secondrange[0] and\
                firstrange[1] >= secondrange[1]) or \
                (secondrange[0] <= firstrange[0] and\
                secondrange[1] >= firstrange[1]):
                count += 1
        return count
            


def parttwo():
    with open('./data/day4') as f:
        count = 0
        for line in f.readlines():
            elves = line.split(',')

            firstrange = range_string_to_int(elves[0])
            secondrange = range_string_to_int(elves[1])

            firstlist = list(range(firstrange[0], firstrange[1]+1))
            secondlist = list(range(secondrange[0], secondrange[1]+1))
            for i in firstlist:
                if i in secondlist:
                    count += 1
                    break

            
        return count


if __name__ == "__main__":
    print("The solution to part one is: ", partone())
    print("The solution to part two is: ", parttwo())