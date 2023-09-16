class Solution:
    def maxProfit(self, prices):
        """Finds greatest positive difference between a pair of integers i and j
        in a list l where l[i] < l[j] and l.index(i) < l.index(j) in O(n) space
        and O(n) time."""
        profit = 0
        while prices:
            sell_price = max(prices)
            sell_date = prices.index(sell_price)
            candidate = prices[:sell_date + 1]
            potential_profit = max(candidate) - min(candidate)
            del prices[:sell_date + 1]
            if potential_profit > profit:
                profit = potential_profit
            if prices:
                buy_price = min(prices)
                buy_date = prices.index(buy_price)
                candidate = prices[buy_date:]
                potential_profit = max(candidate) - min(candidate)
                del prices[buy_date:]
                if potential_profit > profit:
                    profit = potential_profit
        return profit
