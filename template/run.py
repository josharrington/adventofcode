import os
from functools import lru_cache

class MyClass():
    def __init__(self, file: str):
        self.lines = open(file, 'r').read().splitlines()

    def part1(self):
        pass

    def part2(self):
        pass

if __name__ == "__main__":
    mc = MyClass('input.txt')
    print(f"Part 1: {mc.part1()}")
    print(f"Part 2: {mc.part2()}")