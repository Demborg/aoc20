import re
from sys import stdin

between = lambda l, h: lambda x: l <= int(x) <= h
required = {
    "byr": ("(\d{4})", between(1920, 2002)),
    "iyr": ("(\d{4})", between(2010, 2020)),
    "eyr": ("(\d{4})", between(2020, 2030)),
    "hgt": ("(\d*)(in|cm)", lambda x, m: between(*((150, 193) if m =="cm" else (59, 76)))(x)),
    "hcl": ("#[\da-f]{6}", lambda: True),
    "ecl": ("amb|blu|brn|gry|grn|hzl|oth", lambda: True),
    "pid": ("\d{9}", lambda: True)
}
data = [{(t := d.split(":"))[0]: t[1] for d in p.split() if d} for p in stdin.read().replace("\n", " ").split("  ") if p]
print(sum(all(r in d for r in required) for d in data))

print(sum(all(r in d and (m := re.fullmatch(v[0], d[r])) and v[1](*m.groups()) for r, v in required.items()) for d in data))
