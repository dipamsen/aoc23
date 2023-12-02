def parse_games(file):
    allgames = []
    for line in file:
        game, _, data = line.partition(": ")
        gameid = int(game.split(" ")[-1])
        sets = list(
            map(lambda x: x.strip(),
                data.split("; ")))

        currgame = {"id": gameid, "sets": []}
        allgames.append(currgame)
        for set in sets:
            currset = {}
            tokens: list[str] = set.split(", ")
            for token in tokens:
                num, col = token.split(" ")
                currset[col] = int(num)
            currgame["sets"].append(
                (currset.get("red", 0),
                 currset.get("green", 0),
                 currset.get("blue", 0)))

    return allgames


def part_one(file):
    total = 0
    games = parse_games(file)
    for game in games:
        for r, g, b in game["sets"]:
            if r > 12 or g > 13 or b > 14:
                break
        else:
            total += game["id"]
    return total


def part_two(file):
    total = 0
    games = parse_games(file)
    for game in games:
        red = [r for r, g, b in game["sets"]]
        green = [g for r, g, b in game["sets"]]
        blue = [b for r, g, b in game["sets"]]
        minset = max(red), max(green), max(blue)
        power = minset[0] * minset[1] * minset[2]
        total += power
    return total
