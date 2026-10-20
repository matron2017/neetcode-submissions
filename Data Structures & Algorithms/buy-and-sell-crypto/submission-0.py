class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0 
        n = len(prices)
        for i in range(1, n): # i = 3
            num = prices[i]   # num 3
            print(f"i = {i}, num = {num}")
            if num < lowest:
                lowest = num
                continue                
            if num - lowest > profit:   # 3 - 1
                profit = num - lowest # 5
            print(f" profit= {profit}")
        print(profit)
        return profit