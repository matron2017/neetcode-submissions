from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #which 2 mistakes last time?
        # [1, 2l, 3r, 4, 5]
        def eat_bananas(k):
            total_h = 0
            for pile in piles:
                total_h += ceil(pile / k) 
        
            return total_h <= h
        
        l = 1
        r = max(piles)
        #double check this
        while l < r:
            m = (l+r) // 2

            if eat_bananas(m):
                r = m
            else:
                l = m + 1
        
        return r
        

