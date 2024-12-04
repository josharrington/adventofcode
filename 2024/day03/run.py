import re
from functools import lru_cache

class Day03():
    def __init__(self, file: str):
        self.lines = open(file, 'r').read().splitlines()

    def part1(self):
        total = 0
        for line in self.lines:
            for match in re.finditer(r'mul\(\d{1,3},\d{1,3}\)', line):
                nums = re.findall(r'\d+', match.group())
                total += int(nums[0]) * int(nums[1])
        return total

    def part2(self):
        total = 0
        disable = False
        for line in self.lines:
            for match in re.finditer(r'mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)', line):
                print(f"Found: {match.group()}")
                if "don't" in match.group():
                    disable = True
                    continue
                if "do" in match.group():
                    disable = False
                    continue
                if disable:
                    continue
                nums = re.findall(r'\d+', match.group())
                total += int(nums[0]) * int(nums[1])
        return total

if __name__ == "__main__":
    mc = Day03('2024/day03/input.txt')
    print(f"Part 1: {mc.part1()}")
    print(f"Part 2: {mc.part2()}")