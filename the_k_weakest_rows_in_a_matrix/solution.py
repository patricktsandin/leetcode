from operator import itemgetter


class Solution:
    """
    Returns the 'weakest' k rows in matrix mat where row i is stronger than
    row j if:
    sum(mat[i]) > sum(mat[j])
    or sum(mat[i]) = sum(mat[j]) and i > j
    """
    def kWeakestRows(self, mat: list, k: int) -> list:
        for row_id, row in enumerate(mat):
            mat[row_id] = [sum(mat[row_id]), row_id]
        mat.sort(key=itemgetter(0, 1))
        return [row[1] for row in mat[:k]]
