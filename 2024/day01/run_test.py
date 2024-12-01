import pytest
from .run import Day01

def test_1():
    mc = Day01("input_test.txt")
    assert mc.part1() == 11

def test_2():
    mc = Day01("input_test.txt")
    assert mc.part2() == 31