import re


def get_bounds(
        xs: tuple[int,
                  int], y: int, lines: list[str]
) -> list[tuple[int, int]]:
    w = len(lines[0])
    h = len(lines)
    x1, x2 = xs
    # c  c c c c c c c c c  c
    # c x1               x2-1 c
    # c  c c c c c c c c c  c
    bounds = []
    rightfree = False
    leftfree = False
    if x1 > 0:
        bounds.append((x1 - 1, y))
        leftfree = True
    if x2 < w:
        bounds.append((x2, y))
        rightfree = True
    if y > 0:
        for x in range(x1, x2):
            bounds.append((x, y - 1))
        if leftfree:
            bounds.append((x1 - 1, y - 1))
        if rightfree: bounds.append((x2, y - 1))
    if y < h - 1:
        for x in range(x1, x2):
            bounds.append((x, y + 1))
        if leftfree:
            bounds.append((x1 - 1, y + 1))
        if rightfree: bounds.append((x2, y + 1))
    return bounds


def get_nums(file):
    file.seek(0)
    nums = []
    for i, line in enumerate(file):
        digre = re.compile(r"\d+")
        for mat in digre.finditer(line):
            nums.append({
                "num": int(mat.group()),
                "loc": {
                    "x": mat.span(),
                    "y": i
                }
            })
    return nums


def part_one(file):
    lines = list(
        map(lambda x: x.strip(),
            file.readlines()))

    total = 0

    nums = get_nums(file)
    for num in nums:
        bounds = get_bounds(num["loc"]["x"],
                            num["loc"]["y"],
                            lines)
        for x, y in bounds:
            char = lines[y][x]
            if not char.isdigit() and char != ".":
                break
        else:
            continue
        total += num["num"]

    return total


def part_two(file):
    total = 0

    lines = file.readlines()
    gears = []
    for y, line in enumerate(lines):
        matches = re.compile(r"\*").finditer(line)
        gears += [(g.span()[0], y)
                  for g in matches]
    nums = get_nums(file)
    gearparts = {}
    for num in nums:
        for b in get_bounds(num["loc"]["x"],
                            num["loc"]["y"],
                            lines):
            if b in gears:
                if b not in gearparts:
                    gearparts[b] = []
                gearparts[b] += [num]
    for gear, parts in gearparts.items():
        if len(parts) == 2:
            total += parts[0]["num"] * parts[1][
                "num"]

    return total
