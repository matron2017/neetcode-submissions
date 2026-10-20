class Solution:
    def search(self, nums: List[int], target: int) -> int:  
        l = 0
        n = len(nums)
        r = n - 1
        m = (r+l) // 2
        while r >= l:
            mid = nums[m]
            if mid != target:
                if target > mid:
                    l = m + 1
                    m = (r+l) // 2
                else:
                    r = m - 1
                    m = (r+l) // 2
            else:
                return m
        return -1