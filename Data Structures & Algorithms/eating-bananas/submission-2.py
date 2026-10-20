import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def valid_k(k):
            sum_h = 0
            for pile in piles:
                sum_h += math.ceil(pile/k) 
            return sum_h <= h

        l = 1
        r = max(piles)
        m = 1
        while r >= l:
            if valid_k(m):
                smallest = m
                r = m - 1
                m = (l+r) // 2
            else:
                l = m + 1
                m = (l+r) // 2
        
        return smallest