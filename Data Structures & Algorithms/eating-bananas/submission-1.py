import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours <= h

        l = 1
        r = max(piles)
        k = 1

        while r >= l:
            if k_works(k):
                k_latest = k
                r = k - 1
                k = (l+r) // 2
            else:
                l = k + 1
                k = (l+r) // 2
                
        return k_latest



