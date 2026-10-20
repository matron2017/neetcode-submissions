class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        n = len(nums)
        r = n - 1

        while l <= r:
            m = (l+r) // 2
            mid = nums[m]
            
            if mid != target:
                if mid > target:
                    r = m - 1
                else:
                    l = m + 1
                    
            else:
                return m
        
        return -1