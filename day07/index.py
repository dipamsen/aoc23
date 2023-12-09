HALT = True


def part_one(file):
    hands = []
    for line in file:
        hand, bid = line.split()
        hands.append((hand, bid))

    # hands = hands.sort()
