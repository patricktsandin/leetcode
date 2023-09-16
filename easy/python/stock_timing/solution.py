class Solution:
    """Finds greatest positive difference between a pair of integers i and j
    in a list l where l[i] < l[j] and l.index(i) < l.index(j) in O(1) space
    and O(n^2) time."""
    def maxProfit(self, prices):
        profit = 0
        for day, price in enumerate(prices):
            if prices[day + 1:]:
                test_profit = max(prices[day + 1:]) - price
                if test_profit > profit:
                    profit = test_profit
        return profit
