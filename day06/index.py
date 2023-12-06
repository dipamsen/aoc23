import math


def strict_ceil(x):
    return math.ceil(x) if x % 1 != 0 else int(x + 1)


def strict_floor(x):
    return math.floor(x) if x % 1 != 0 else int(x - 1)


def parse_file(file):
    time, dist = list(
        map(lambda x: list(map(int, x.split()[1:])), file.readlines()))
    records = {}
    for t, d in zip(time, dist):
        records[t] = d
    return records


def find_numways(t, d):
    # t = total time
    # x = mash time
    # t - x = rest time
    # velocity gained = x
    # so, distance = (t-x)*x = tx - x^2
    # To find: num of x for which tx - x^2 > d
    # x^2 - tx + d < 0 for 0 < x < t
    # roots: (t +- sqrt(t^2 - 4d))/2 = a, b
    # find x for which a < x < b (x is an integer)
    a = (t - math.sqrt(t*t - 4*d))/2
    b = (t + math.sqrt(t*t - 4*d))/2
    numways = strict_floor(b) - strict_ceil(a) + 1
    return numways


def part_one(file):
    records = parse_file(file)
    product = 1
    for t, d in records.items():
        numways = find_numways(t, d)
        product *= numways
    return product


def part_two(file):
    records = parse_file(file)
    time = int("".join(map(str, records.keys())))
    dist = int("".join(map(str, records.values())))
    return find_numways(time, dist)
