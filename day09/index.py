def part_one(file):
    seqs = []
    total = 0
    for line in file:
        if line:
            seqs.append(list(map(int, line.split())))
    for seq in seqs:
        total += get_next_num(seq)
    return total


def part_one(file):
    seqs = []
    total = 0
    for line in file:
        if line:
            seqs.append(list(map(int, line.split())))
    for seq in seqs:
        total += get_first_num(seq)
    return total


def get_next_num(seq):
    # seq = [0, 3, 6, 9, 12, 15]
    diffs = [seq[i] - seq[i - 1] for i in range(1, len(seq))]
    if len(set(diffs)) == 1:
        return seq[-1] + diffs[0]
    else:
        next_diff = get_next_num(diffs)
        return seq[-1] + next_diff


def get_first_num(seq):
    # seq = [0, 3, 6, 9, 12, 15]
    diffs = [seq[i] - seq[i - 1] for i in range(1, len(seq))]
    if len(set(diffs)) == 1:
        return seq[0] - diffs[0]
    else:
        first_diff = get_first_num(diffs)
        return seq[0] - first_diff
