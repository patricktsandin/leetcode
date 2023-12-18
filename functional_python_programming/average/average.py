"""Functional Python Programming 3e

Chapter 1, Example Set 1

Convert the following to functional form:
def average(v: list[float]) -> float:
    '''Averages a list of numbers.'''
    assert len(v) >= 1

    n = len(v)
    s = 0
    i = 0
    while i != n:
        s = s + v[i]
        i = i + 1
    m = s/n
    return m
"""

from unittest import TestCase


def average(numbers: list[float]) -> float:
    """Averages a list of numbers."""
    assert numbers

    return sum(numbers)/len(numbers)


class TestAverage(TestCase):
    def test_average(self) -> None:
        expected = 7.5
        result = average(
            [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
        )
        self.assertAlmostEqual(expected, result)
