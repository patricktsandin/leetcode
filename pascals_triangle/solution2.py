class Solution:
    def generate(self, numRows):
        """Returns Pascal's triangle in list form with the given number of rows
        in O(n^2) space and time."""
        triangle = []
        for row in range(1, numRows + 1):
            level = []
            element = 1
            level.append(element)
            for column in range(1, row):
                element = (element*(row - column))//column
                level.append(element)
            triangle.append(level)
        return triangle
