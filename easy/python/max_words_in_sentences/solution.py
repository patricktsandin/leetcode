"""
A sentence is a list of words that are separated by a single space with no
leading or trailing spaces.
You are given an array of strings sentences, where each sentences[i]
represents a single sentence.
Return the maximum number of words that appear in a single sentence.
"""

from unittest import TestCase
from typing import List


class Solution:
    """Solves iteratively in linear time and constant space."""

    @staticmethod
    def most_words_found(sentences: List[str]) -> int:
        """
        Find wordcount of longest sentence.
        :param sentences: sentences to check
        :return: wordcount
        """
        assert len(sentences) >= 1

        return max(sentence.count(" ") for sentence in sentences) + 1


class TestMaxWordsInSentences(TestCase):
    def test_minimum_input(self):
        expected = 1
        result = Solution.most_words_found(["a"])
        self.assertEqual(expected, result)

    def test_typical_input_1(self):
        expected = 4
        result = Solution.most_words_found(["this is", "a test to see", "if"])
        self.assertEqual(expected, result)

    def test_typical_input_2(self):
        expected = 6
        result = Solution.most_words_found(["a a", "b", "c c c", "d d d d d d"])
        self.assertEqual(expected, result)
