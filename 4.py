import re
from sys import stdin

required = {
    "byr": ("(\d{4})", lambda x: 1920 <= int(x) <= 2002),
    "iyr": ("(\d{4})", lambda x: 2010 <= int(x) <= 2020),
    "eyr": ("(\d{4})", lambda x: 2020 <= int(x) <= 2030),
    "hgt": ("(\d*)(in|cm)", lambda x, m: (150 if m == "cm" else 59) <= int(x) <= (193 if m == "cm" else 76)),
    "hcl": ("#[\da-f]{6}", lambda: True),
    "ecl": ("amb|blu|brn|gry|grn|hzl|oth", lambda: True),
    "pid": ("\d{9}", lambda: True)
}
data = [{(t := d.split(":"))[0]: t[1] for d in p.split() if d} for p in stdin.read().replace("\n", " ").split("  ") if p]
print(sum(1 for d in data if all(r in d for r in required)))

print(sum(1 for d in data if all(r in d and (m := re.fullmatch(v[0], d[r])) and v[1](*m.groups()) for r, v in required.items())))
