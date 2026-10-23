from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def eat_bananas(k):
            eat_h = 0
            for pile in piles:
                eat_h += ceil(pile / k)
            
            return eat_h <= h
        
        l = 1
        r = max(piles)

        while l < r:
            m = (l+r) // 2
            if eat_bananas(m):
                r = m
            else:
                l = m + 1
        
        return r


        

