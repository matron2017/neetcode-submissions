from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def valid_k(k):
            sum_k = 0
            for pile in piles:
                sum_k += ceil(pile / k) 
            return sum_k <= h 
        
        l = 1
        r = max(piles)
        smallest_k = r
        while r >= l:
            m = (l+r) // 2
            if valid_k(m):
                smallest_k = m
                r = m - 1
            else:
                l = m + 1

        return smallest_k
                
