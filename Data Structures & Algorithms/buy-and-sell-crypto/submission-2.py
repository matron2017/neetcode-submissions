class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0 
        n = len(prices)
        for i in range(1, n):
            num = prices[i]   
            if num < lowest:
                lowest = num
                continue               
            if num - lowest > profit:   
                profit = num - lowest 
        return profit