def part_one(file):
    score = 0
    for line in file:
        card, _, data = line.partition(": ")
        winner, _, nums = data.partition(" | ")
        nums = [int(n) for n in nums.split()]
        winner = [int(n) for n in winner.split()]
        id = card.split()[1]
        wincount = 0
        for num in nums:
            if num in winner:
                wincount += 1
        if wincount > 0:
            score += 2**(wincount - 1)
    return score


def part_two(file):
    lines = file.readlines()
    cardcount = [1] * len(lines)
    parsed = []
    for line in lines:
        card, _, data = line.partition(": ")
        winner, _, nums = data.partition(" | ")
        nums = [int(n) for n in nums.split()]
        winner = [int(n) for n in winner.split()]
        id = int(card.split()[1])
        wincount = 0
        for num in nums:
            if num in winner:
                wincount += 1

        parsed.append(
            (id, winner, nums, wincount))

    for id, wins, nums, wc in parsed:
        for i in range(wc):
            cardcount[id + i] += cardcount[id - 1]

    return sum(cardcount)
