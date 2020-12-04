import re
from sys import stdin

required = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
data = [{(t := d.split(":"))[0]: t[1] for d in p.split() if d} for p in stdin.read().replace("\n", " ").split("  ") if p]
print(sum(1 for d in data if all(r in d for r in required)))
