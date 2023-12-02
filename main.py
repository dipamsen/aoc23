import importlib
import os

lastday = 0
for day in range(1, 31):
    dirname = f"day{day:02d}"
    if os.path.exists(dirname):
        lastday = day
    else:
        break


def fopen(path):
    if os.path.exists(path):
        return open(path)


if lastday > 0:
    print(f"Day {lastday}")
    print()
    dirname = f"day{lastday:02d}"
    mod = importlib.import_module(
        f"{dirname}.index")

    inp = fopen(f"{dirname}/input.txt")
    e1 = fopen(f"{dirname}/example.txt")
    e2 = fopen(f"{dirname}/example2.txt")

    if "part_one" in dir(mod) and (inp or e1):
        print("Part 1:")
        for name, file in ({
                "Example": e1,
                "Final": inp
        }).items():
            ans = mod.part_one(file)
            print(f"\t{name}: {ans}")
        print()

    if "part_two" in dir(mod) and (inp or e2
                                   or e1):
        print("Part 2:")
        for name, file in ({
                "Example": e2 or e1,
                "Final": inp
        }).items():
            file.seek(0)
            ans = mod.part_two(file)
            print(f"\t{name}: {ans}")
        print()
