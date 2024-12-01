import pytest
from .run import MyClass

def test_1():
    mc = MyClass("input_test.txt")
    assert 1 == 1

def test_2():
    mc = MyClass("input_test.txt")
    assert 1 == 1