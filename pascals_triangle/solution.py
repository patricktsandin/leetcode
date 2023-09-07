class Solution:
    def generate(self, numRows):
        """Returns Pascal's triangle in list form with the given number of rows
        in O(n^2) space and time."""
        triangle = []
        for row in range(numRows):
            triangle.append(list())
            counter = row
            while counter > -1:
                if counter == row or counter == 0:
                    triangle[row].append(1)
                else:
                    triangle[row].insert(
                        1, sum(triangle[row - 1][counter - 1:counter + 1])
                    )
                counter -= 1
        return triangle