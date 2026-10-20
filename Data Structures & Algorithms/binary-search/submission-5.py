class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)   
        l = 0
        r = n -1
        m = (l+r) // 2
        while l <= r:
            mid = nums[m]
            if target != mid:
                if target > mid:
                    l = m + 1
                    m = (l+r) // 2
                else:
                    r = m - 1
                    m = (l+r) // 2
            else:
                return m
        
        return -1