import pytest
from .run import Day02

def test_1():
    mc = Day02("input_test.txt")
    assert mc.part1() == 2

def test_2():
    mc = Day02("input_test.txt")
    assert mc.part2() == 6