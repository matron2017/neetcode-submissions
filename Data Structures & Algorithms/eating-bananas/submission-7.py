from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def eat_in_h(k):
            total_h = 0
            for num in piles:
                total_h += ceil(num / k)
            
            return total_h <= h
        

        l = 1
        r = max(piles)
        while l < r:
            m = (l+r) // 2
            if eat_in_h(m):
                r = m
            else:
                l = m + 1

    
        return r

