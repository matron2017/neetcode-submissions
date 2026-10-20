class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # go throguh , l r and m,
        # at point where l and r conflict  (m+-1)
        # then stop and return fasle
        # otherwise return correct
        
        l = 0
        n = len(nums)
        r = n - 1
        m = (l+r) // 2
        while l <= r:
            mid = nums[m]
            if mid != target:
                if mid > target:
                    r = m - 1
                    m = (l+r) // 2
                else:
                    l = m + 1
                    m = (l+r) // 2
            else:
                return m
        return -1