import os
from functools import lru_cache

class Day02():
    def __init__(self, file: str):
        lines = open(file, 'r').read().splitlines()
        self.reports = []
        for line in lines:
            self.reports.append(
                [int(x) for x in line.split(' ') if x]
            )

    def check_report(self, report):
        increasing = report[0] < report[1]

        for i, num in enumerate(report):
            if i+1 == len(report):
                break
            next_num = report[i+1]

            if any([
                num == next_num,
                increasing and num > next_num,
                not increasing and num < next_num,
                abs(num-next_num) > 3,
            ]):
                return False
        return True

    def part1(self):
        safe_count = 0
        for report in self.reports:
            safe_count += 1 if self.check_report(report) else 0
        return safe_count

    def part2(self):
        safe_count = 0
        for report in self.reports:
            for i in range(0, len(report)):
                if self.check_report(report[:i] + report[i+1:]):
                    safe_count += 1
                    break
        return safe_count

if __name__ == "__main__":
    mc = Day02('/home/josh/projects/adventofcode/2024/day02/input.txt')
    print(f"Part 1: {mc.part1()}")
    print(f"Part 2: {mc.part2()}")