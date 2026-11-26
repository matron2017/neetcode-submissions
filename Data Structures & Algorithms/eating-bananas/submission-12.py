from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def eat_bananas(k):
            h_eat = 0
            for pile in piles:
                h_eat += ceil(pile / k)

            return h_eat <= h

        l = 1
        r = max(piles)

        while l < r:
            m = (l+r) // 2
            
            if eat_bananas(m):
                r = m
            else:
                l = m + 1
        
        return r
