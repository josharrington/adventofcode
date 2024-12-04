import pytest
from .run import Day03

def test_1():
    mc = Day03("input_test.txt")
    assert mc.part1() == 161

def test_2():
    mc = Day03("input_test_2.txt")
    assert mc.part2() == 48