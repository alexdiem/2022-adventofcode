def detect_marker(N):
    with open('./data/day6') as f:
        msg = f.readline()
        for i in range(N, len(msg)):
            marker = msg[i-N:i]
            if len(set(marker)) == len(marker):
                return i


def partone():
    return detect_marker(4)
            
            
def parttwo():
    return detect_marker(14)


if __name__ == "__main__":
    print("The solution to part one is: ", partone())
    print("The solution to part two is: ", parttwo())