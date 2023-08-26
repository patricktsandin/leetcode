class Solution:
    """Finds greatest positive difference between a pair of integers i and j
    in a list l where l[i] < l[j] and l.index(i) < l.index(j) in O(n) space
    and O(n) time."""
    def maxProfit(self, prices):
        candidates = []

        while prices:
            sell_price = max(prices)
            sell_date = prices.index(sell_price)
            candidates.append(prices[:sell_date + 1])
            del prices[:sell_date + 1]
            if prices:
                buy_price = min(prices)
                buy_date = prices.index(buy_price)
                candidates.append(prices[buy_date:])
                del prices[buy_date:]

        profit = 0
        for prices in candidates:
            potential_profit = max(prices) - min(prices)
            if potential_profit > profit:
                profit = potential_profit
        return profit