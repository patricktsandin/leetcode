"""
You own a Goal Parser that can interpret a string command. The command
consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal
Parser will interpret "G" as the string "G", "()" as the string "o",
and "(al)" as the string "al". The interpreted strings are then concatenated
in the original order.

Given the string command, return the Goal Parser's interpretation of command.
"""

from unittest import TestCase


class Solution:
    """Solves iteratively in linear time and space."""
    @staticmethod
    def interpret(command: str) -> str:
        """Returns translated string"""
        return command.replace("()", "o").replace("(al)", "al")


class TestGoalParser(TestCase):
    def test_g(self):
        expected = "G"
        result = Solution.interpret("G")
        self.assertEqual(expected, result)

    def test_o(self):
        expected = "o"
        result = Solution.interpret("()")
        self.assertEqual(expected, result)

    def test_al(self):
        expected = "al"
        result = Solution.interpret("(al)")
        self.assertEqual(expected, result)

    def test_goal(self):
        expected = "Goal"
        result = Solution.interpret("G()(al)")
        self.assertEqual(expected, result)
