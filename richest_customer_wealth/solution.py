class Solution:
    """Return sum of largest row in matrix"""
    def maximumWealth(self, accounts):
        return max([sum(account) for account in accounts])
