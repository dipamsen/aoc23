const fs = require("fs");

const input = fs.readFileSync("./input.txt", "utf8");

const hands = [];
for (const line of input.split("\n")) {
  const [hand, bid] = line.split(/\s+/);
  hands.push({ hand, bid });
}

function handType(hand) {
  // Five of a kind, where all five cards have the same label: AAAAA
  // Four of a kind, where four cards have the same label and one card has a different label: AA8AA
  // Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
  // Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
  // Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
  // One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
  // High card
  counter = {};
  for (const card of hand) {
    counter[card] = counter[card] ? counter[card] + 1 : 1;
  }
  let wildcard = counter["J"] || 0;
  delete counter["J"];
  const values = Object.values(counter);
  const max = Math.max(...values);
  let added = false;
  const uVals =
    values.length > 0
      ? values.map((v) => {
          if (v === max && !added) {
            added = true;
            return v + wildcard;
          }
          return v;
        })
      : [wildcard];
  const uniqueValueCount = uVals.length;
  if (uniqueValueCount === 1) {
    return 10;
  }
  if (uniqueValueCount === 2) {
    if (uVals.includes(4)) {
      return 9;
    }
    return 8;
  }
  if (uniqueValueCount === 3) {
    if (uVals.includes(3)) {
      return 7;
    }
    return 6;
  }
  if (uniqueValueCount === 4) {
    return 5;
  }
  return 4;
}

const cardStrength = {
  A: "E",
  K: "D",
  Q: "C",
  T: "A",
  9: "9",
  8: "8",
  7: "7",
  6: "6",
  5: "5",
  4: "4",
  3: "3",
  2: "2",
  J: "1",
};

function sortHands(a, b) {
  const aType = handType(a.hand);
  const bType = handType(b.hand);
  if (aType === bType) {
    const ahex = a.hand
      .split("")
      .map((c) => cardStrength[c])
      .join("");
    const bhex = b.hand
      .split("")
      .map((c) => cardStrength[c])
      .join("");
    const aStrength = parseInt(ahex, 16);
    const bStrength = parseInt(bhex, 16);
    // console.log(aStrength, bStrength);
    return aStrength < bStrength ? -1 : 1;
  }
  return aType < bType ? -1 : 1;
}

const sorted = hands.sort(sortHands);
console.log(sorted.reduce((p, c, i) => p + c.bid * (i + 1), 0));
