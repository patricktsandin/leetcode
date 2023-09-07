class Solution:
    """Returns Pascal's triangle in list form with the given number of rows
    in O(n^2) space and time."""
    def generate(self, numRows):
        triangle = []
        for row in range(numRows):
            triangle.append(list())
            counter = num_elements = row
            while counter > -1:
                if counter == num_elements:
                    triangle[row].append(1)
                elif counter == 0:
                    triangle[row].append(1)
                else:
                    next_num = (
                            triangle[row - 1][counter - 1]
                            + triangle[row - 1][counter]
                    )
                    triangle[row].insert(1, next_num)
                counter -= 1
        return triangle