class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_in = None
        for i in range(len(prices)):
            curr = prices[i]
            if buy_in == None:
                buy_in = curr
                continue
            if buy_in > curr:
                buy_in = curr
            if curr - buy_in > max_profit:
                max_profit = curr - buy_in
        return max_profit
