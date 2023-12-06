const fs = require("fs");

function parse(fileContent) {
  const parts = fileContent.split("\n\n").map((x) => x.trim());
  const seedLine = parts.shift();
  const seeds = seedLine.split(": ")[1].split(" ").map(Number);

  const rules = [];
  parts.forEach((part) => {
    const lines = part.split("\n");
    const kind = lines[0].split(" ")[0].split("-");
    const kindTuple = [kind[0], kind[kind.length - 1]];

    const mapper = (val) => {
      for (let line of lines.slice(1)) {
        const [dst, src, rng] = line.split(" ").map(Number);
        if (src <= val && val <= src + rng - 1) {
          return val - src + dst;
        }
      }
      return val;
    };

    rules.push([kindTuple, mapper]);
  });

  return [seeds, rules];
}

const input = fs.readFileSync("./day05/input.txt", "utf-8").replace(/\r/g, "");

const [seeds, rules] = parse(input);

const locs = [];
for (const s of seeds) {
  let x = s;
  for (const [kind, mapper] of rules) {
    x = mapper(x);
  }
  locs.push(x);
}
console.log(Math.min(...locs));
