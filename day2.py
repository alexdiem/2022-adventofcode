def partone():
    WIN = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    DRAW = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    PTS_PLAY = {'X': 1, 'Y': 2, 'Z': 3}
    PTS_WIN = 6
    PTS_DRAW = 3

    points = 0
    with open('data/day2') as f:
        for line in f.readlines():
            play = line.split()
            points += PTS_PLAY[play[1]]

            if WIN[play[0]] == play[1]:
                points += PTS_WIN
            elif DRAW[play[0]] == play[1]:
                points += PTS_DRAW

    return points


def parttwo():
    STRATEGY = {'X': 0, 'Y': 3, 'Z': 6}
    WIN = {'A': 'B', 'B': 'C', 'C': 'A'}
    LOOSE = {'A': 'C', 'B': 'A', 'C': 'B'}
    PTS_PLAY = {'A': 1, 'B': 2, 'C': 3}

    points = 0
    with open('data/day2') as f:
        for line in f.readlines():
            play = line.split()
            points += STRATEGY[play[1]]

            if STRATEGY[play[1]] == 0:
                points += PTS_PLAY[LOOSE[play[0]]]
            elif STRATEGY[play[1]] == 3:
                points += PTS_PLAY[play[0]]
            else:
                points += PTS_PLAY[WIN[play[0]]]

    return points


if __name__ == "__main__":
    print("The solution to part one is: ", partone())
    print("The solution to part two is: ", parttwo())