from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def valid_k(k):
            sum_h = 0
            for pile in piles:
                sum_h += ceil(pile / k)
            return sum_h <= h

        l = 1
        r = max(piles)
        smallest_k = r
        while r >= l:
            # 1 2 3 4
            m = (l+r) // 2
            if valid_k(m):
                smallest_k = m
                r = m - 1
            else:
                l = m + 1
        return smallest_k  
