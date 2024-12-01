import os

class Day01():
    def __init__(self, file: str):
        self.left = []
        self.right = []

        for line in open(file, 'r'):
            if len(line) == 0:
                pass
            left, right = [x for x in line.split(' ') if x]
            self.left.append(int(left))
            self.right.append(int(right))

    def part1(self) -> int:
        sum_of_diff = 0
        s_left = sorted(self.left)
        s_right = sorted(self.right)
        for i in range(len(s_left)):
            sum_of_diff += max(s_left[i], s_right[i]) - min(s_left[i], s_right[i])
        return sum_of_diff

    def part2(self) -> int:
        occurances = {}
        similarity_score = 0

        for num in self.right:
            if occurances.get(num):
                occurances[num] += 1
            else:
                occurances[num] = 1

        for num in self.left:
            similarity_score += occurances.get(num, 0) * num

        return similarity_score


if __name__ == "__main__":
    mc = Day01('./input.txt')
    print(f"Part 1: {mc.part1()}")
    print(f"Part 2: {mc.part2()}")