class Solution:
    """
    Returns the 'weakest' k rows in matrix mat where row i is stronger than
    row j if:
    sum(mat[i]) > sum(mat[j])
    or sum(mat[i]) = sum(mat[j]) and i > j
    """

    def kWeakestRows(self, mat: list, k: int) -> list:
        return sorted(range(len(mat)), key=lambda i: mat[i])[:k]
