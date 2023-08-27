class Solution:
    def maxProfit(self, prices):
        """Finds greatest positive difference between a pair of integers i and j
        in a list l where l[i] < l[j] and l.index(i) < l.index(j) in O(1) space
        and O(n) time."""
        profit = 0
        best_buy_price = float("inf")
        best_sell_price = float("-inf")
        for price in prices:
            if price < best_buy_price:
                best_buy_price = price
                best_sell_price = price
            elif price > best_sell_price:
                best_sell_price = price
                potential_profit = best_sell_price - best_buy_price
                if potential_profit > profit:
                    profit = potential_profit
        return profit
