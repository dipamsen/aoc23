import itertools


def parse(file):
    parts = [x.strip() for x in file.read().split("\n\n")]
    seeds = list(map(int, parts.pop(0).partition(": ")[-1].split(" ")))
    rules = []
    for part in parts:
        part = part.split("\n")
        kind = part.pop(0).split(" ")[0].split("-")
        kind = (kind[0], kind[-1])

        # https://docs.python-guide.org/writing/gotchas/#late-binding-closures
        def mapper(val, part=part):
            for line in part:
                dst, src, rng = list(map(int, (line.split(" "))))
                if src <= val <= src + rng - 1:
                    return val - src + dst
            return val

        rules.append((kind, mapper))
    return seeds, rules


def main(seeds, rules):
    locs = []
    for s in seeds:
        var = s
        for kind, mapper in rules:
            var = mapper(var)
        locs.append(var)

    return min(locs)


def part_one(file):
    seeds, rules = parse(file)
    return main(seeds, rules)


# HALT = True


def part_two(file):
    seedsrng, rules = parse(file)
    seeds = itertools.chain(*[range(s, s + seedsrng[i*2+1])
                              for i, s in enumerate(seedsrng[::2])])
    return main(seeds, rules)
