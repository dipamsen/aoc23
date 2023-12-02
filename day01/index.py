import io

digs = list('0123456789')


def get_first_dig(str):
    for ch in str:
        if ch in digs:
            return ch


def get_last_dig(str):
    for ch in str[::-1]:
        if ch in digs:
            return ch


def part_one(file: io.TextIOWrapper):
    sum = 0
    for line in file:
        num = int(
            get_first_dig(line) +
            get_last_dig(line))
        sum += num
    return sum


def getnums(str):
    nums = list("0123456789")
    names = [
        "one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine"
    ]

    p = 0
    numlist = []
    while len(str) > p:
        if str[p] in nums:
            numlist.append(int(str[p]))
            p += 1
            continue
        a = str[p:p + 3]
        b = str[p:p + 4]
        c = str[p:p + 5]
        for sub in [a, b, c]:
            if sub in names:
                numlist.append(
                    names.index(sub) + 1)
                p += 1
                continue
        p += 1
    return numlist


def part_two(file: io.TextIOWrapper):
    sum = 0
    for line in file:
        if line:
            nums = getnums(line)
            a = nums[0]
            b = nums[-1]
            sum += a * 10 + b
    return sum
