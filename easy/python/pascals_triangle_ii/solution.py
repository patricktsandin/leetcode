from typing import List


class Solution:
    def getRow(self, row_index: int) -> List[int]:
        """
        Returns given row of Pascal's Triangle using iterative algorithm
        in linear time and space.
        :param row_index: 0-indexed row number of Pascal's Triangle
        :return: list of integers comprising a row in Pascal's Triangle
        """
        level = []
        element = 1
        level.append(element)
        for column in range(1, row_index + 1):
            element = (element*(row_index + 1 - column))//column
            level.append(element)
        return level
